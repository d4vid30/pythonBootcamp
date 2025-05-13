import pandas as pd
import matplotlib.pyplot as plt
import os
# Leer el archivo CSV
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/clima.csv')

# Crear gráfica con dos ejes
fig, ax1 = plt.subplots()

# Línea de temperatura
ax1.plot(df['dia'], df['temperatura'], marker='o', label='Temperatura')
ax1.set_xlabel('Día')
ax1.set_ylabel('Temperatura (°C)')
ax1.grid(True)

# Eje secundario para lluvia
ax2 = ax1.twinx()
ax2.bar(df['dia'], df['lluvia'], alpha=0.3, label='Lluvia')
ax2.set_ylabel('Lluvia (mm)')

# Combinar leyendas
lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, loc='upper left')
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/graficas"
nombre_archivo = "clima.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/clima.png")
plt.show()