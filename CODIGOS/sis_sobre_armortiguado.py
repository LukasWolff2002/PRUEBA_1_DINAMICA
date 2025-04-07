import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0      # masa (kg)
k = 1.1     # rigidez (N/m)
zeta = 1.1   # coeficiente de amortiguamiento (ζ > 1 → sobreamortiguado)

# Condiciones iniciales
u0 = 1.0     # desplazamiento inicial (m)
v0 = 1.0     # velocidad inicial (m/s)

# Frecuencia natural
omega_n = np.sqrt(k / m)

# Raíces del sistema sobreamortiguado
r1 = -omega_n * (zeta - np.sqrt(zeta**2 - 1))
r2 = -omega_n * (zeta + np.sqrt(zeta**2 - 1))

# Coeficientes A1 y A2 usando condiciones iniciales
A = np.array([[1, 1],
              [r1, r2]])
b = np.array([u0, v0])
A1, A2 = np.linalg.solve(A, b)

# Tiempo
t = np.linspace(0, 10, 500)

# Solución analítica
u = A1 * np.exp(r1 * t) + A2 * np.exp(r2 * t)
v = A1 * r1 * np.exp(r1 * t) + A2 * r2 * np.exp(r2 * t)
a = A1 * r1**2 * np.exp(r1 * t) + A2 * r2**2 * np.exp(r2 * t)

# Gráfica
plt.figure(figsize=(12, 5))
plt.plot(t, u, label=fr"$u(t) = A_1 e^{{{r1:.2f} t}} + A_2 e^{{{r2:.2f} t}}$")
plt.plot(t, v, label=r"$\dot{u}(t) = A_1 r_1 e^{r_1 t} + A_2 r_2 e^{r_2 t}$")
plt.plot(t, a, label=r"$\ddot{u}(t) = A_1 r_1^2 e^{r_1 t} + A_2 r_2^2 e^{r_2 t}$")

plt.title(f"Sistema Sobreamortiguado: $u_0$ = {u0} m, $\dot{{u}}_0$ = {v0} m/s, $\zeta$ = {zeta}")
plt.xlabel("Tiempo [s]")
plt.ylabel("Respuesta (u, v, a)")
plt.grid(True)

# Leyenda a la derecha centrada
plt.legend(loc='center right', borderaxespad=1.0)

plt.tight_layout()
plt.savefig(f"INFORME/GRAFICOS/sis_sobreamortiguado_u0_{u0}_v0_{v0}_zeta_{zeta}.png", dpi=300)
plt.show()
