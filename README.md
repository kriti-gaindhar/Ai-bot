---
title: AI-BOT
emoji: 🤖
colorFrom: indigo
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
---

# AI-BOT

This repo contains:
- A Streamlit UI in `app.py` (Gemini API)
- A FastAPI server in `inference.py` (OpenEnv-style endpoints)

## Deploy to Hugging Face Spaces (recommended: Streamlit)

Hugging Face may not show a “Streamlit” SDK option (you might only see **Gradio / Docker / Static**). In that case, use **Docker**.

## Deploy to Hugging Face Spaces (Docker: UI + API)

This repo’s Docker setup runs both:
- Streamlit UI at `/`
- FastAPI endpoints at `/openenv/*` and `/reset` `/step` `/state`

This repo also includes `openenv.yaml` at the repo root for OpenEnv validation.

Steps:
1. Create a new Space on Hugging Face.
2. Choose **SDK: Docker**.
3. Add a Space **Secret**:
   - `GOOGLE_API_KEY` = your Gemini API key
4. Push/upload the repo contents.

Important:
- Hugging Face expects the file to be named **Dockerfile** (exact casing).

This repo already includes `Dockerfile`.

Then push to the Space.

## Local run

### Streamlit
- `pip install -r requirements.txt`
- `streamlit run app.py`

### FastAPI
- `pip install -r requirements.txt`
- `uvicorn inference:app --host 0.0.0.0 --port 7860`
