import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0      # masa (kg)
k = 10.0     # rigidez (N/m)

# Condiciones iniciales
u0 = 1.0     # desplazamiento inicial (m)
v0 = 0.0     # velocidad inicial (m/s)

# Frecuencia natural
omega_n = np.sqrt(k / m)

# Tiempo
t = np.linspace(0, 10, 500)

# Solución analítica
u = u0 * np.cos(omega_n * t) + (v0 / omega_n) * np.sin(omega_n * t)
v = (-u0 * omega_n * np.sin(omega_n * t) + v0 * np.cos(omega_n * t))
a = (-u0 * omega_n**2 * np.cos(omega_n * t) - v0 * omega_n * np.sin(omega_n * t))

# Gráfica
plt.figure(figsize=(12, 5))
plt.plot(t, u, label=r"$u(t) = u_0 \cos(\omega_n t) + \frac{\dot{u}_0}{\omega_n} \sin(\omega_n t)$")
plt.plot(t, v, label=r"$v(t) = -u_0 \omega_n \sin(\omega_n t) + \dot{u}_0 \cos(\omega_n t)$")
plt.plot(t, a, label=r"$a(t) = -u_0 \omega_n^2 \cos(\omega_n t) - \dot{u}_0 \omega_n \sin(\omega_n t)$")

plt.title(f"$u_0$ = {u0} m, $\dot{{u}}_0$ = {v0} m/s ")
plt.xlabel("Tiempo [s]")
plt.ylabel("Respuesta (u, v, a)")
plt.grid(True)

# Leyenda a la derecha centrada
plt.legend(loc='center right', borderaxespad=1.0)

plt.tight_layout()
plt.savefig(f"INFORME/GRAFICOS/sis_no_amortiguado_u0_{u0}_v0_{v0}.png", dpi=300)
plt.show()
