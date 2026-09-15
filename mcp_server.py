# ============================================================
# mcp_server.py — Serveur MCP (Model Context Protocol)
# Port : 8000
# Rôle : Fournir des données à l'agent IA via une API REST
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

# --- Création de l'application FastAPI ---
app = FastAPI(
    title="Serveur MCP",
    description="Serveur MCP qui fournit des données à l'agent IA Athena",
    version="1.0.0"
)

# --- CORS : autorise le widget HTML à communiquer avec ce serveur ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# ENDPOINT 1 — Page d'accueil
# URL : http://localhost:8000/
# ============================================================
@app.get("/")
def accueil():
    return {
        "service": "Serveur MCP",
        "status": "✅ En ligne",
        "port": 8000,
        "description": "Je fournis des données à l'agent IA Athena",
        "endpoints": ["/", "/data"]
    }

# ============================================================
# ENDPOINT 2 — Données principales
# URL : http://localhost:8000/data
# Rôle : Appelle une API externe et retourne les données
# ============================================================
@app.get("/data")
async def get_data():
    # On appelle une API externe publique (activité aléatoire)
    url = "https://www.boredapi.com/api/activity"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            data = response.json()
            
            return {
                "source": "API Externe (BoredAPI)",
                "status": "✅ Données reçues",
                "contenu": {
                    "activite": data.get("activity", "Non disponible"),
                    "type": data.get("type", "Non disponible"),
                    "participants": data.get("participants", 0),
                    "accessibilite": data.get("accessibility", 0)
                },
                "mcp_info": {
                    "serveur": "MCP Port 8000",
                    "protocole": "REST/HTTP"
                }
            }
    
    except Exception as e:
        # Si l'API externe est indisponible, on retourne des données de secours
        return {
            "source": "Données locales (API externe indisponible)",
            "status": "⚠️ Mode secours",
            "contenu": {
                "activite": "Apprendre FastAPI et MCP",
                "type": "education",
                "participants": 1,
                "accessibilite": 0.0
            },
            "mcp_info": {
                "serveur": "MCP Port 8000",
                "protocole": "REST/HTTP"
            },
            "erreur": str(e)
        }

# ============================================================
# LANCEMENT DU SERVEUR (si on lance ce fichier directement)
# ============================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=8000, reload=True)