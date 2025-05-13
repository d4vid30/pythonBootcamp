import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Gráfico de línea simple

# valores = [3, 7, 1, 5, 12]  
# plt.plot(valores)  
# plt.title('Gráfico de Línea Simple')  
# plt.xlabel('Índice')  
# plt.ylabel('Valor')  
# plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/linea.png")  
# plt.show()

# 2. Gráfico de barras

# cursos = ['A', 'B', 'C', 'D', 'E'] 
# cantidad = [30, 25, 40, 20, 35]  

# plt.bar(cursos, cantidad)  
# plt.title('Cantidad de Estudiantes por Curso') 
# plt.xlabel('Curso') 
# plt.ylabel('Cantidad de Estudiantes')  
# plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/barras.png")  # Guarda la figura
# plt.show()  

# 3. Gráfico de dispersión (scatter plot)


# x = np.random.rand(50)  
# y = np.random.rand(50)  
# plt.scatter(x, y)  
# plt.title('Gráfico de Dispersión de Números Aleatorios')  
# plt.xlabel('Valores de X')  
# plt.ylabel('Valores de Y')  
# plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/disperso.png")  
# plt.show()  

# 4. Subplots

fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # Crea la figura y los subplots

# Subplot 1: Senoidal
x = np.linspace(0, 4 * np.pi, 100)  
y_sin = np.sin(x)  
axs[0].plot(x, y_sin) 
axs[0].set_title('Función Senoidal')  
axs[0].set_xlabel('x')  
axs[0].set_ylabel('sin(x)')  
axs[0].grid(True)  

# Subplot 2: Cuadrática
x = np.linspace(-5, 5, 100)  
y_cuad = x**2  
axs[1].plot(x, y_cuad)  
axs[1].set_title('Función Cuadrática') 
axs[1].set_xlabel('x')  
axs[1].set_ylabel('x^2')  
axs[1].grid(True)  

plt.tight_layout()  
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/subplots.png")  
plt.show()  