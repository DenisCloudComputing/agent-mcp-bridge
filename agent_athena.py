# ============================================================
# agent_athena.py — Agent IA Athena
# Port : 8001
# Rôle : Reçoit les questions du widget HTML,
#         interroge le serveur MCP (port 8000),
#         retourne une réponse enrichie
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

# --- URL du serveur MCP ---
MCP_SERVER_URL = "http://localhost:8000"

# --- Création de l'application FastAPI ---
app = FastAPI(
    title="Agent IA Athena",
    description="Agent IA qui interroge le serveur MCP et enrichit les données",
    version="1.0.0"
)

# --- CORS : autorise le widget HTML à communiquer avec cet agent ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# ENDPOINT 1 — Page d'accueil de l'agent
# URL : http://localhost:8001/
# ============================================================
@app.get("/")
def accueil():
    return {
        "agent": "Athena IA",
        "status": "✅ En ligne",
        "port": 8001,
        "description": "Je suis l'agent IA qui connecte le widget au serveur MCP",
        "mcp_connecte": MCP_SERVER_URL,
        "endpoints": ["/", "/ask"]
    }

# ============================================================
# ENDPOINT 2 — Question à l'agent
# URL : http://localhost:8001/ask
# Rôle : Interroge le MCP et retourne une réponse enrichie
# ============================================================
@app.get("/ask")
async def ask():
    try:
        # --- Étape 1 : L'agent appelle le serveur MCP ---
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{MCP_SERVER_URL}/data",
                timeout=10.0
            )
            mcp_data = response.json()

        # --- Étape 2 : L'agent enrichit les données ---
        contenu = mcp_data.get("contenu", {})
        activite = contenu.get("activite", "inconnue")
        type_activite = contenu.get("type", "inconnu")
        participants = contenu.get("participants", 0)
        accessibilite = contenu.get("accessibilite", 0)

        # --- Étape 3 : L'agent génère une réponse intelligente ---
        if accessibilite <= 0.25:
            niveau = "🟢 Très accessible"
        elif accessibilite <= 0.5:
            niveau = "🟡 Modérément accessible"
        elif accessibilite <= 0.75:
            niveau = "🟠 Peu accessible"
        else:
            niveau = "🔴 Difficile d'accès"

        if participants == 1:
            groupe = "activité solo"
        elif participants <= 3:
            groupe = "petit groupe"
        else:
            groupe = "grand groupe"

        # --- Étape 4 : Retourne la réponse complète au widget ---
        return {
            "agent": "Athena IA",
            "status": "✅ Réponse générée",
            "analyse": {
                "activite_suggeree": activite,
                "categorie": type_activite,
                "format": groupe,
                "accessibilite": niveau,
                "conseil": f"💡 Athena suggère : '{activite}' — parfait pour un {groupe} !"
            },
            "source_mcp": {
                "url": f"{MCP_SERVER_URL}/data",
                "status": mcp_data.get("status", "inconnu"),
                "source_api": mcp_data.get("source", "inconnue")
            },
            "architecture": "Widget → Agent Athena :8001 → MCP :8000 → API Externe"
        }

    except Exception as e:
        return {
            "agent": "Athena IA",
            "status": "❌ Erreur",
            "erreur": str(e),
            "conseil": "⚠️ Vérifie que le serveur MCP tourne sur le port 8000",
            "architecture": "Widget → Agent Athena :8001 → MCP :8000 → API Externe"
        }

# ============================================================
# LANCEMENT DU SERVEUR (si on lance ce fichier directement)
# ============================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("agent_athena:app", host="0.0.0.0", port=8001, reload=True)