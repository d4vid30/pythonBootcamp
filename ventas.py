import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer archivo CSV (debe llamarse exactamente 'ventas.csv' y estar en la misma carpeta)
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/ventas.csv')
print("✅ Archivo ventas.csv cargado correctamente")

# Crear figura y ejes
fig, ax = plt.subplots()

# Graficar cada producto como una línea
ax.plot(df['mes'], df['producto_a'], marker='o', label='Producto A')
ax.plot(df['mes'], df['producto_b'], marker='o', label='Producto B')
ax.plot(df['mes'], df['producto_c'], marker='o', label='Producto C')

# Etiquetas y título
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas')
ax.set_title('Ventas Mensuales por Producto')
ax.legend()
ax.grid(True)

# Ajustar y mostrar
plt.tight_layout()
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "ventas.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/ventas.png")
plt.show()
