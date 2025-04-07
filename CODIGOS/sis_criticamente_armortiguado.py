import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0      # masa (kg)
k = 1.1    # rigidez (N/m)

# Condiciones iniciales
u0 = 1.0     # desplazamiento inicial (m)
v0 = 0.0     # velocidad inicial (m/s)

# Frecuencia natural
omega_n = np.sqrt(k / m)

# Tiempo
t = np.linspace(0, 10, 500)

# Solución analítica para sistema críticamente amortiguado
u = np.exp(-omega_n * t) * (u0 * (1 + omega_n * t) + v0 * t)
v = np.exp(-omega_n * t) * (
    -omega_n * (u0 * (1 + omega_n * t) + v0 * t) + u0 * omega_n + v0
)
a = np.exp(-omega_n * t) * (
    omega_n**2 * (u0 * (1 + omega_n * t) + v0 * t)
    - 2 * omega_n * (u0 * omega_n + v0)
)

# Gráfica
plt.figure(figsize=(12, 5))

plt.plot(t, u, label=r"$u(t) = e^{-\omega_n t} \left[ u_0 (1 + \omega_n t) + \dot{u}_0\, t \right]$")
plt.plot(t, v, label=r"$\dot{u}(t) = e^{-\omega_n t} \left[ -\omega_n \left( u_0 (1 + \omega_n t) + \dot{u}_0\, t \right) + u_0 \omega_n + \dot{u}_0 \right]$")
plt.plot(t, a, label=r"$\ddot{u}(t) = e^{-\omega_n t} \left[ \omega_n^2 \left( u_0 (1 + \omega_n t) + \dot{u}_0\, t \right) - 2 \omega_n (u_0 \omega_n + \dot{u}_0) \right]$")

plt.title(f"Sistema Críticamente Amortiguado: $u_0$ = {u0} m, $\dot{{u}}_0$ = {v0} m/s")
plt.xlabel("Tiempo [s]")
plt.ylabel("Respuesta (u, v, a)")
plt.grid(True)

# Leyenda a la derecha centrada
plt.legend(loc='center right', borderaxespad=1.0)

plt.tight_layout()
plt.savefig(f"INFORME/GRAFICOS/sis_criticamente_amortiguado_u0_{u0}_v0_{v0}.png", dpi=300)
plt.show()
