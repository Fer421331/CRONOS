print(">>> SERVER.PY DE CRONOS CARGADO <<<")


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"status": "ok", "state": new_state}
