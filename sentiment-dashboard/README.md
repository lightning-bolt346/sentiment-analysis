# Sentiment Dashboard

A minimal full-stack scaffold for a sentiment analysis dashboard.

## Structure

- `frontend/` static client (HTML/CSS/JS)
- `backend/` FastAPI server exposing `/analyze`

## Run backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Open frontend

Open `frontend/index.html` in a browser (use a static server if needed).

On Linux/macOS you can run from repo root:

```bash
python -m http.server 5173 --directory frontend
```

Then visit `http://localhost:5173`.

## API

- `POST /analyze` with body `{ "text": "string" }` returns sentiment and key phrases.