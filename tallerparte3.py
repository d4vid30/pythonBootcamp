import pandas as pd
import matplotlib.pyplot as plt
import os

# Parte 3: Lectura de archivos con Pandas

# 9. Cargar archivo y mostrar las primeras 5 filas
# Usa un archivo.csv llamado datos_ventas.csv
df = pd.read_csv('C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/datos/datos_ventas.csv')  # Asegúrate de que el archivo esté en la misma carpeta o proporciona la ruta correcta
print("Primeras 5 filas:")
print(df.head())

# 10. Estadísticas básicas
print("\nEstadísticas básicas:")
print(f"Total de ventas: {df['Ventas'].sum()}")
print(f"Promedio de precio: {df['Precio'].mean()}")
producto_mas_vendido = df.loc[df['Ventas'].idxmax(), 'Producto']
print(f"Producto más vendido: {producto_mas_vendido}")

# 11. Filtrar datos
# Muestra solo los productos vendidos en el mes de enero (Fecha empieza por 2025-01).
print("\nProductos vendidos en enero:")
productos_enero = df[df['Fecha'].str.startswith('2025-01')]
print(productos_enero)

# 12. Gráfica de barras con Pandas
# Grafica la cantidad total vendida por producto. (Agrupa por Producto y suma las ventas).
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()
ventas_por_producto.plot(kind='bar')
plt.title('Total de Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Total de Ventas')
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/ventas_por_producto.png")    
plt.show()