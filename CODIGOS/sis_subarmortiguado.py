import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0      # masa (kg)
k = 10.0     # rigidez (N/m)
zeta = 0.1   # coeficiente de amortiguamiento (ζ < 1 → subamortiguado)

# Condiciones iniciales
u0 = 1.0     # desplazamiento inicial (m)
v0 = 1.0     # velocidad inicial (m/s)

# Frecuencias
omega_n = np.sqrt(k / m)
omega_d = omega_n * np.sqrt(1 - zeta**2)

# Coeficientes A y B a partir de condiciones iniciales
A = u0
B = (v0 + zeta * omega_n * u0) / omega_d

# Tiempo
t = np.linspace(0, 10, 500)

# Solución analítica
u = np.exp(-zeta * omega_n * t) * (A * np.cos(omega_d * t) + B * np.sin(omega_d * t))
v = np.exp(-zeta * omega_n * t) * (
    -A * omega_d * np.sin(omega_d * t)
    + B * omega_d * np.cos(omega_d * t)
) - zeta * omega_n * u

a = -2 * zeta * omega_n * v - omega_n**2 * u

# Gráfica
plt.figure(figsize=(12, 5))
plt.plot(t, u, label=fr"$u(t) = e^{{-\zeta \omega_n t}} \left( A \cos(\omega_d t) + B \sin(\omega_d t) \right)$")
plt.plot(t, v, label=r"$v(t) = \dot{u}(t)$")
plt.plot(t, a, label=r"$a(t) = \ddot{u}(t)$")

plt.title(f"Sistema Subamortiguado: $u_0$ = {u0} m, $\dot{{u}}_0$ = {v0} m/s, $\zeta$ = {zeta}")
plt.xlabel("Tiempo [s]")
plt.ylabel("Respuesta (u, v, a)")
plt.grid(True)

# Leyenda a la derecha centrada
plt.legend(loc='center right', borderaxespad=1.0)

plt.tight_layout()
plt.savefig(f"INFORME/GRAFICOS/sis_subamortiguado_u0_{u0}_v0_{v0}_zeta_{zeta}.png", dpi=300)
plt.show()
