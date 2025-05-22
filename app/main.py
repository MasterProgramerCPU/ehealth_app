from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app import routes  # presupunem că ai toate rutele acolo

app = FastAPI()

# Servire fișiere statice (ex: CSS, JS, imagini)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurare template engine Jinja2
templates = Jinja2Templates(directory="app/templates")

# Include rutele tale definite în `routes.py`
app.include_router(routes.router)

# CORS (opțional, dacă folosești frontend separat sau HTMX cu interacțiuni async)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # înlocuiește cu domeniul tău în producție
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

