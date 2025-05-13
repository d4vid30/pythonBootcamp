import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Leer archivo CSV (debe llamarse exactamente 'salud.csv' y estar en la misma carpeta)
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/fitness.csv')
print("✅ Archivo fitness.csv cargado correctamente")

# Preparar posiciones para las barras
x = np.arange(len(df))
ancho = 0.25

# Crear figura y ejes
fig, ax = plt.subplots()

# Barras para cada métrica
ax.bar(x - ancho, df['edad'], width=ancho, label='Edad')
ax.bar(x,        df['frecuencia_cardiaca'], width=ancho, label='Frecuencia cardíaca')
ax.bar(x + ancho,df['maximo_oxigeno'],      width=ancho, label='Máximo oxígeno')

# Etiquetas, título y ticks
ax.set_xlabel('Persona')
ax.set_ylabel('Valor')
ax.set_title('Indicadores de Salud por Persona')
ax.set_xticks(x)
ax.set_xticklabels(df['persona'], rotation=45)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "fitness.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/fitness.png")
plt.show()
