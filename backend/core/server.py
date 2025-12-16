print(">>> SERVER.PY DE CRONOS CARGADO <<<")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.state import get_state, set_state

app = FastAPI(
    title="C.R.O.N.O.S. Core",
    description="Cerebro central de CRONOS",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "C.R.O.N.O.S. Core activo"}

@app.get("/state")
def state():
    return get_state()

@app.post("/state/{new_state}")
def update_state(new_state: str):
    set_state(new_state)
    return {"ok": True, "state": new_state}
