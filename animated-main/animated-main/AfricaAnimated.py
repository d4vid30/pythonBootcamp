import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# --- PARÁMETROS ---
csv_path = "C:/Users/Natalia/OneDrive/Attachments/repo/animated-main/animated-main/01 renewable-share-energy.csv"
countries = ["United States", "China", "Africa"]  # Ahora incluye tres entidades
colors = ['green', 'blue', 'orange']              # Un color por cada una
output_gif = "us_china_africa_renewables.gif"

# Cargar el archivo CSV
df = pd.read_csv(csv_path)

# Filtrar datos para cada entidad y ordenar por año
dfs = {}
for country in countries:
    df_c = df[df["Entity"] == country].copy()
    df_c = df_c.sort_values("Year")
    dfs[country] = df_c

# Usamos el rango de años de la primera entidad (puedes comprobar que coincida)
years = dfs[countries[0]]["Year"].values

# Extraer los valores de renovables para cada entidad
renewables = {
    country: dfs[country]["Renewables (% equivalent primary energy)"].values
    for country in countries
}

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(
    0,
    max(renewables[countries[0]].max(),
        renewables[countries[1]].max(),
        renewables[countries[2]].max()
    ) + 5
)
ax.set_title("Energía Renovable: US vs China vs Africa")
ax.set_xlabel("Año")
ax.set_ylabel("Renovables (% energía primaria)")
ax.grid(True)

# Líneas para cada entidad
lines = {}
for country, color in zip(countries, colors):
    line, = ax.plot([], [], lw=2, color=color, label=country)
    lines[country] = line
ax.legend(loc="upper left")

# Texto con año y valores
text = ax.text(0.05, 0.80, '', transform=ax.transAxes, va='top')

# Inicialización
def init():
    for line in lines.values():
        line.set_data([], [])
    text.set_text('')
    return list(lines.values()) + [text]

# Actualización por frame
def update(frame):
    year = years[frame]
    for country in countries:
        x = years[:frame+1]
        y = renewables[country][:frame+1]
        lines[country].set_data(x, y)
    # Mostrar año y cada porcentaje
    info = [f"{c}: {renewables[c][frame]:.2f}%" for c in countries]
    text.set_text(f"Año: {year}\n" + "\n".join(info))
    return list(lines.values()) + [text]

# Crear y guardar la animación
ani = FuncAnimation(
    fig, update,
    frames=len(years),
    init_func=init,
    blit=True,
    interval=150
)
ani.save(output_gif, writer="pillow", fps=5)

# plt.show()  # Si quieres verlo en pantalla
