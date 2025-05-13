import pandas as pd
import matplotlib.pyplot as plt
import os
# Leer archivo CSV (archivo en la misma carpeta que este script)
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/combustible.csv')
print("✅ Archivo consumo.csv cargado correctamente")

# Crear figura
graf, ax = plt.subplots()

# Gráfico de línea: Litros usados vs Distancia
ax.plot(df['distancia_km'], df['litros_usados'], marker='o', label='Litros usados')
ax.set_xlabel('Distancia (km)')
ax.set_ylabel('Litros usados')
ax.set_title('Consumo de Combustible vs Distancia')
ax.grid(True)
ax.legend()

plt.tight_layout()
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "combustible.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/combustible.png")
plt.show()