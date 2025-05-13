import matplotlib.pyplot as plt
import numpy as np

# Parte 2: Cálculos y gráficos con NumPy

# 5. Generar datos y graficar una función
x = np.linspace(-10, 10, 100)
y = x**2 - 3*x + 2
plt.plot(x, y)
plt.title('Gráfico de la función y = x^2 - 3x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/funcion.png")
plt.show()

# 6. Comparación de funciones
x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title('Comparación de sin(x) y cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/sin_cos.png")
plt.show()

# 7. Operaciones entre arrays
vector1 = np.random.randint(0, 100, 100)
vector2 = np.random.randint(0, 100, 100)

suma_total = np.sum(vector1 + vector2)
valor_maximo = np.max(np.concatenate((vector1, vector2)))
desviacion_estandar = np.std(np.concatenate((vector1, vector2)))

print(f"Suma total: {suma_total}")
print(f"Valor máximo: {valor_maximo}")
print(f"Desviación estándar: {desviacion_estandar}")

# 8. Histograma con NumPy
datos = np.random.normal(0, 1, 1000)
plt.hist(datos, bins=30, density=True, alpha=0.6, color='g')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia Normalizada')
plt.grid(True)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/histograma.png")
plt.show()