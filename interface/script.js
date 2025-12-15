// ===============================
// C.R.O.N.O.S. STATE MACHINE v1.0
// ===============================

const CRONOS = {
  state: 'idle',

  elements: {
    core: document.getElementById('cronos'),
    status: document.getElementById('status')
  },

  setState(newState) {
    if (this.state === newState) return;

    this._exitState(this.state);
    this.state = newState;
    this._enterState(newState);
  },

  _enterState(state) {
    switch (state) {
      case 'idle':
        this.elements.core.classList.remove('speaking');
        this.elements.status.textContent = 'ACTIVO · EN SILENCIO';
        break;

      case 'speaking':
        this.elements.core.classList.add('speaking');
        this.elements.status.textContent = 'HABLANDO';
        break;

      case 'listening':
        this.elements.status.textContent = 'ESCUCHANDO';
        break;

      case 'thinking':
        this.elements.status.textContent = 'PROCESANDO';
        break;

      case 'error':
        this.elements.status.textContent = 'ERROR DEL SISTEMA';
        break;

      default:
        console.warn(`Estado desconocido: ${state}`);
    }
  },

  _exitState(state) {
    // Espacio para limpieza futura (timers, audio, etc.)
  }
};

// ===============================
// PRUEBA CONTROLADA (TEMPORAL)
// ===============================

setTimeout(() => CRONOS.setState('speaking'), 3000);
setTimeout(() => CRONOS.setState('idle'), 9000);

// ===============================
// CONTROLES MANUALES (DEV MODE)
// ===============================

document.querySelectorAll('[data-state]').forEach(button => {
  button.addEventListener('click', () => {
    const state = button.getAttribute('data-state');
    CRONOS.setState(state);
  });
});
