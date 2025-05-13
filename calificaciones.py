import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Leer archivo CSV (debe llamarse exactamente 'notas.csv' y estar en la misma carpeta)
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/notas.csv')
print("✅ Archivo notas.csv cargado correctamente")

# Preparar posiciones para las barras
x = np.arange(len(df))
ancho = 0.25

# Crear figura y ejes
fig, ax = plt.subplots()

# Barras para cada evaluación
ax.bar(x - ancho, df['parcial_1'], width=ancho, label='Parcial 1')
ax.bar(x,        df['parcial_2'], width=ancho, label='Parcial 2')
ax.bar(x + ancho,df['final'],    width=ancho, label='Examen Final')

# Etiquetas, título y ticks
ax.set_xlabel('Estudiante')
ax.set_ylabel('Calificación')
ax.set_title('Comparación de Calificaciones por Estudiante')
ax.set_xticks(x)
ax.set_xticklabels(df['nombre'], rotation=45, ha='right')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "calificaciones.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/calificaciones.png")
plt.show()
