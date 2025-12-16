cronos_state = {
    "state": "idle"
}

def set_state(state: str):
    cronos_state["state"] = state

def get_state():
    return cronos_state
