# mcp_server.py — Serveur MCP Earthquake
# Port 8000

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="MCP Earthquake Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def accueil():
    return {
        "service": "MCP Earthquake Server",
        "status": "✅ En ligne",
        "port": 8000,
        "endpoints": ["/", "/earthquakes"]
    }

@app.get("/earthquakes")
async def get_earthquakes(
    minmagnitude: float = Query(default=4.0, description="Magnitude minimale"),
    limit: int = Query(default=10, description="Nombre de résultats"),
    period: str = Query(default="week", description="Période: day, week, month")
):
    url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{_get_feed(minmagnitude, period)}.geojson"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            raw = response.json()

        features = raw.get("features", [])[:limit]
        earthquakes = []

        for f in features:
            props = f.get("properties", {})
            geo = f.get("geometry", {}).get("coordinates", [0, 0, 0])
            earthquakes.append({
                "lieu": props.get("place", "Inconnu"),
                "magnitude": props.get("mag", 0),
                "profondeur_km": round(geo[2], 1) if len(geo) > 2 else 0,
                "heure_utc": props.get("time", 0),
                "alerte": props.get("alert", "aucune"),
                "tsunami": "⚠️ Oui" if props.get("tsunami", 0) == 1 else "Non",
                "url_detail": props.get("url", "")
            })

        return {
            "source": "USGS Earthquake Hazards Program",
            "status": "✅ Données reçues",
            "periode": period,
            "magnitude_min": minmagnitude,
            "total": len(earthquakes),
            "earthquakes": earthquakes
        }

    except Exception as e:
        return {
            "source": "USGS",
            "status": "❌ Erreur",
            "erreur": str(e),
            "earthquakes": []
        }

def _get_feed(mag: float, period: str) -> str:
    if mag >= 7.0:
        level = "significant"
    elif mag >= 4.5:
        level = "4.5"
    elif mag >= 2.5:
        level = "2.5"
    else:
        level = "all"
    return f"{level}_{period}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=8000, reload=True)