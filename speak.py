from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="C.R.O.N.O.S. Core",
    description="Cerebro central de C.R.O.N.O.S.",
    version="0.1.0"
)

# Permitir comunicación con el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se limita
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estado global de CRONOS
cronos_state = {
    "state": "idle"
}

@app.get("/")
def root():
    return {"message": "C.R.O.N.O.S. Core activo"}

@app.get("/state")
def get_state():
    return cronos_state

@app.post("/state/{new_state}")
def set_state(new_state: str):
    cronos_state["state"] = new_state
    return {
        "status": "ok",
        "new_state": new_state
    }
