import matplotlib.pyplot as plt
import numpy as np
import os
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()
x = np.linspace(0, 10, 100) # 1-- puentos entre 0  y 10 
y = np.sin(x) 
plt.plot(x, y)
plt.title('Seno')
plt.xlabel('x')
plt.ylabel('sen(x)')
plt.grid(True)
carpeta_destino = "C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
nombre_archivo = "frist.png"
ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
plt.savefig("C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas/frist.png")
plt.show()