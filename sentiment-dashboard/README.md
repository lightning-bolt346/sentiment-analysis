# Sentiment Analysis Dashboard

A minimal full-stack scaffold for a sentiment analysis dashboard.

## Structure

- frontend: static UI with simple modules
- backend: FastAPI API with placeholder analyzer and extractor

## Quickstart

### Backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

### Frontend

Serve `frontend/` via any static server (or configure FastAPI static mount later).

```bash
python -m http.server 8001 --directory frontend
```

Then open `http://localhost:8001` and set API base to `http://localhost:8000/api` if needed.
