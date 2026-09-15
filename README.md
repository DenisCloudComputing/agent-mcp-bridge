# 📍 CRÉER LE `README.md` COMPLET

> 💡 **C'est quoi le README.md ?**
> C'est la **carte d'identité** de ton projet sur GitHub. C'est la première chose que les gens voient quand ils visitent ton repo. Il doit être clair, professionnel et expliquer comment installer et utiliser le projet.

---

### 🔷 ACTION 1 — Ouvre le fichier README.md

> 📍 OÙ : VS CODE — PANNEAU EXPLORER (colonne de gauche)

**Fais ceci :**
1. Dans le panneau de gauche, tu vois déjà `README.md`
2. **Clique dessus** pour l'ouvrir
3. Il contient peut-être juste le titre du repo mis par GitHub

**✅ Ce que tu dois voir :**
Le fichier `README.md` s'ouvre à droite dans VS Code.

---

### 🔷 ACTION 2 — Sélectionne tout et remplace

> 📍 OÙ : VS CODE — FICHIER `README.md`

**Fais ceci :**
1. Clique dans la zone du fichier à droite
2. Appuie sur `CTRL + A` pour **tout sélectionner**
3. Appuie sur `SUPPR` pour **tout effacer**
4. Le fichier est maintenant vide

---

### 🔷 ACTION 3 — Colle le nouveau README

> 📍 OÙ : VS CODE — FICHIER `README.md`

**Colle exactement ce contenu :**

```markdown
# 🤖 Agent IA & Serveur MCP — agent-mcp-bridge

> Projet de démonstration : un agent IA connecté à un serveur MCP via FastAPI, avec un widget HTML/JS interactif.

---

## 🏗️ Architecture

```
Widget (HTML/JS) → Agent IA (FastAPI :8001) → Serveur MCP (FastAPI :8000) → API Externe
```

- **Widget** (`widget.html`) → Interface utilisateur interactive (thème sombre)
- **Agent IA** (`agent_athena.py`) → Cerveau du système, enrichit les données, port 8001
- **Serveur MCP** (`mcp_server.py`) → Fournit les données via API REST, port 8000
- **API Externe** → [BoredAPI](https://www.boredapi.com/) → activités aléatoires

---

## ⚙️ Stack technique

| Technologie     | Rôle                        |
|-----------------|-----------------------------|
| Python 3.x      | Langage principal           |
| FastAPI         | Framework API (MCP + Agent) |
| Uvicorn         | Serveur ASGI pour FastAPI   |
| HTTPX           | Requêtes HTTP asynchrones   |
| HTML / CSS / JS | Widget interactif frontend  |

---

## 📁 Structure du projet

```
agent-mcp-bridge/
│
├── .venv/               ← Environnement virtuel (pas sur GitHub)
├── mcp_server.py        ← Serveur MCP (port 8000)
├── agent_athena.py      ← Agent IA Athena (port 8001)
├── widget.html          ← Widget interactif HTML/JS
├── requirements.txt     ← Dépendances Python
├── .gitignore           ← Fichiers exclus de Git
└── README.md            ← Documentation du projet
```

---

## 🚀 Installation

### 📋 Prérequis
- Python 3.x installé
- Git installé

### 1️⃣ Clone le repo

```bash
git clone https://github.com/DenisCloudComputing/agent-mcp-bridge.git
cd agent-mcp-bridge
```

### 2️⃣ Crée et active l'environnement virtuel

**Windows (PowerShell) :**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux / Mac :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> ✅ Tu dois voir `(.venv)` au début de la ligne dans ton terminal.

### 3️⃣ Installe les dépendances

```bash
pip install -r requirements.txt
```

---

## ⚡ Démarrage

> ⚠️ Tu as besoin de **2 terminaux séparés** ouverts en même temps.

### 🖥️ Terminal 1 — Lance le Serveur MCP

```bash
uvicorn mcp_server:app --port 8000 --reload
```

✅ Résultat attendu :
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 🖥️ Terminal 2 — Lance l'Agent IA

```bash
uvicorn agent_athena:app --port 8001 --reload
```

✅ Résultat attendu :
```
INFO:     Uvicorn running on http://0.0.0.0:8001
```

### 🌐 Ouvre le Widget

Ouvre le fichier `widget.html` directement dans ton navigateur
(double-clique dessus depuis l'explorateur de fichiers)

---

## 🔗 Liens utiles

| Lien | Description |
|------|-------------|
| [http://localhost:8000](http://localhost:8000) | Serveur MCP — Accueil |
| [http://localhost:8000/data](http://localhost:8000/data) | Serveur MCP — Données |
| [http://localhost:8000/docs](http://localhost:8000/docs) | Serveur MCP — Documentation API |
| [http://localhost:8001](http://localhost:8001) | Agent IA — Accueil |
| [http://localhost:8001/ask](http://localhost:8001/ask) | Agent IA — Interroger |
| [http://localhost:8001/docs](http://localhost:8001/docs) | Agent IA — Documentation API |

---

## 🎯 Comment ça fonctionne

1. Tu ouvres `widget.html` dans ton navigateur
2. Tu cliques sur **"⚡ Interroger l'Agent Athena"**
3. Le widget appelle l'Agent IA sur `http://localhost:8001/ask`
4. L'Agent IA appelle le Serveur MCP sur `http://localhost:8000/data`
5. Le Serveur MCP appelle l'API externe (BoredAPI)
6. Les données remontent jusqu'au widget et s'affichent

---

## 👤 Auteur

**Denis** — [DenisCloudComputing](https://github.com/DenisCloudComputing)

---

## 📄 Licence

MIT — Libre d'utilisation et de modification.
```

---

### 🔷 ACTION 4 — Sauvegarde le fichier

### 🔷 ACTION 5 — Prévisualise le README dans VS Code

> 📍 OÙ : VS CODE — FICHIER `README.md`

**Fais ceci :**
1. Assure-toi d'être sur l'onglet `README.md`
2. Appuie sur `CTRL + SHIFT + V`

**✅ Ce que tu dois voir :**
Un nouvel onglet s'ouvre avec le README mis en forme — titres, tableaux, blocs de code colorés. C'est exactement ce que les gens verront sur GitHub !

> 💡 Si tu veux fermer la prévisualisation, clique simplement sur la croix ✕ de cet onglet.

---

### 🔷 ACTION 6 — Vérifie la structure complète de ton projet

> 📍 OÙ : VS CODE — PANNEAU EXPLORER (colonne de gauche)

**✅ Tu dois maintenant voir exactement ceci :**
```
AGENT-MCP-BRIDGE
├── .venv/
├── agent_athena.py
├── mcp_server.py
├── widget.html
├── requirements.txt
├── .gitignore
└── README.md
```




