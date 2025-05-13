import pandas as pd
import matplotlib.pyplot as plt
import os
# Leer archivo CSV (debe estar en la misma carpeta que este script)
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/datos.csv')
print("✅ Archivo temperatura.csv cargado correctamente")

# Crear figura y ejes
fig, ax = plt.subplots()

# Gráfico de línea: Temperatura vs Tiempo
ax.plot(df['tiempo'], df['temperatura'], marker='o', label='Temperatura')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Temperatura (°C)')
ax.set_title('Temperatura vs Tiempo')
ax.grid(True)
ax.legend()

# Ajustar y mostrar
plt.tight_layout()
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "datos.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/datos.png")
plt.show()
