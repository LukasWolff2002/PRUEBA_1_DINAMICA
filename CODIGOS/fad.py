import numpy as np
import matplotlib.pyplot as plt

# Definir la función FAD(lambda)
def FAD(lambda_val):
    return 1 / (1 - lambda_val**2)

# Rango de valores de lambda (evitar valores cercanos a ±1 para evitar divisiones por cero)
# Rango de valores de lambda entre 0 y 5
lambda_vals = np.linspace(0, 2, 400)
fad_vals = FAD(lambda_vals)

# Graficar la función
plt.figure(figsize=(8, 6))
plt.plot(lambda_vals, fad_vals, label=r'$FAD(\lambda) = \frac{1}{1-\lambda^2}$', color='b')
plt.title('Gráfica de la función FAD(λ) para λ entre 0 y 2')
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$FAD(\lambda)$')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.legend()
#plt.show()
plt.savefig('INFORME/GRAFICOS/FAD.png', dpi=300)  # Guardar la figura como un archivo PNG
