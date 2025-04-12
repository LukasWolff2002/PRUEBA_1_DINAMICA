import numpy as np
import matplotlib.pyplot as plt
from math import log

# Datos proporcionados (solo los valores positivos de Amp)
amp_pos = np.array([6.0, 3.62, 2.19, 1.32, 1.06, 0.79, 0.52])
tiempo_pos = np.array([0.4, 1.6, 2.81, 4.01, 5.22, 6.42, 7.62])

AMP = []

for elemento in amp_pos:
    if elemento > 0:
        AMP.append(log(abs(elemento)))

# Ajuste de la recta lineal (regresión lineal) solo para los datos positivos
m, b = np.polyfit(tiempo_pos, AMP, 1)  # Encuentra la pendiente m y el intercepto b

# Crear la función de la recta ajustada
recta = m * tiempo_pos + b

# Graficar los datos originales y la recta ajustada
plt.figure(figsize=(10, 6))

# Graficar los valores originales
plt.plot(tiempo_pos, AMP, 'bo', label='Datos originales positivos')

# Graficar la recta ajustada
plt.plot(tiempo_pos, recta, 'r-', label=f'Recta ajustada: $y = {m:.2f}x + {b:.2f}$')

# Títulos y etiquetas
plt.title('Ajuste de una recta lineal a los datos positivos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amp (cm)')
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.savefig('INFORME/GRAFICOS/ajuste_recta.png', dpi = 300)  # Guardar la figura como un archivo PNG
