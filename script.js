// ===============================
// CRONOS – Frontend Controller
// ===============================

const API_URL = "http://localhost:8000";

const cronos = document.getElementById("cronos");
const statusText = document.getElementById("status");

let currentState = "idle";

// ===============================
// Actualizar UI según estado
// ===============================
function updateUI(state) {
  cronos.classList.remove(
    "idle",
    "listening",
    "thinking",
    "speaking",
    "error"
  );

  cronos.classList.add(state);

  const labels = {
    idle: "ACTIVO · EN SILENCIO",
    listening: "ESCUCHANDO…",
    thinking: "PROCESANDO…",
    speaking: "HABLANDO",
    error: "ERROR DEL SISTEMA"
  };

  statusText.textContent = labels[state] || state.toUpperCase();
}

// ===============================
// Obtener estado desde backend
// ===============================
async function fetchState() {
  try {
    const res = await fetch(`${API_URL}/state`);
    const data = await res.json();

    if (data.state !== currentState) {
      currentState = data.state;
      updateUI(currentState);
    }
  } catch (err) {
    console.warn("Backend no disponible");
  }
}

// ===============================
// Loop de sincronización
// ===============================
setInterval(fetchState, 300);
