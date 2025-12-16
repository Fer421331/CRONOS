// ===============================
// CRONOS – Frontend Controller
// ===============================

const API_URL = "http://localhost:8000";

const cronos = document.getElementById("cronos");
const statusText = document.getElementById("status");
const buttons = document.querySelectorAll(".controls button");

let currentState = "idle";

// ===============================
// Actualizar UI según estado
// ===============================
function updateUI(state) {
  // limpiar estados previos
  cronos.classList.remove(
    "idle",
    "listening",
    "thinking",
    "speaking",
    "error"
  );

  cronos.classList.add(state);

  // texto humano
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
// Cambiar estado (manual / botones)
// ===============================
async function setState(state) {
  try {
    await fetch(`${API_URL}/state/${state}`, { method: "POST" });
  } catch (err) {
    console.error("No se pudo cambiar el estado");
  }
}

// ===============================
// Botones de prueba
// ===============================
buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    const state = btn.dataset.state;
    setState(state);
  });
});

// ===============================
// Loop de sincronización
// ===============================
setInterval(fetchState, 500);
