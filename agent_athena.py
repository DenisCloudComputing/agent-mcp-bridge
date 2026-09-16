# agent_athena.py — Agent IA Earthquake
# Port 8001

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime

MCP_URL = "http://localhost:8000"

app = FastAPI(title="Athena Earthquake Agent", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def accueil():
    return {
        "agent": "Athena Earthquake Agent",
        "status": "✅ En ligne",
        "port": 8001,
        "mcp": MCP_URL,
        "endpoints": ["/", "/ask", "/search"]
    }

@app.get("/ask")
async def ask(
    minmagnitude: float = Query(default=4.0),
    limit: int = Query(default=10),
    period: str = Query(default="week")
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{MCP_URL}/earthquakes",
                params={"minmagnitude": minmagnitude, "limit": limit, "period": period},
                timeout=15.0
            )
            mcp_data = response.json()

        earthquakes = mcp_data.get("earthquakes", [])

        if not earthquakes:
            return {
                "agent": "Athena",
                "status": "⚠️ Aucune donnée",
                "message": "Aucun séisme trouvé pour ces critères.",
                "earthquakes": []
            }

        magnitudes = [e["magnitude"] for e in earthquakes if e["magnitude"]]
        mag_max = max(magnitudes) if magnitudes else 0
        mag_moy = round(sum(magnitudes) / len(magnitudes), 2) if magnitudes else 0
        tsunamis = sum(1 for e in earthquakes if e["tsunami"] == "⚠️ Oui")

        if mag_max >= 7.0:
            alerte_globale = "🔴 MAJEUR — Séismes très dangereux détectés"
        elif mag_max >= 5.5:
            alerte_globale = "🟠 ÉLEVÉ — Séismes significatifs"
        elif mag_max >= 4.5:
            alerte_globale = "🟡 MODÉRÉ — Séismes notables"
        else:
            alerte_globale = "🟢 FAIBLE — Activité sismique normale"

        return {
            "agent": "Athena Earthquake Agent",
            "status": "✅ Analyse complète",
            "alerte_globale": alerte_globale,
            "statistiques": {
                "total_seismes": len(earthquakes),
                "magnitude_max": mag_max,
                "magnitude_moyenne": mag_moy,
                "alertes_tsunami": tsunamis,
                "periode": period
            },
            "earthquakes": earthquakes,
            "source_mcp": {
                "url": f"{MCP_URL}/earthquakes",
                "source": mcp_data.get("source", "USGS"),
                "status": mcp_data.get("status", "")
            },
            "architecture": "Widget → Agent Athena :8001 → MCP :8000 → USGS API"
        }

    except Exception as e:
        return {
            "agent": "Athena",
            "status": "❌ Erreur",
            "erreur": str(e),
            "earthquakes": []
        }

@app.get("/search")
async def search(
    minmagnitude: float = Query(default=5.0),
    period: str = Query(default="month"),
    limit: int = Query(default=5)
):
    return await ask(minmagnitude=minmagnitude, limit=limit, period=period)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agent_athena:app", host="0.0.0.0", port=8001, reload=True)