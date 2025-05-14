import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import os

# ====================================================================================
# 1. Seno animado con fase desplazada
#    Objetivo: Animar una onda seno que cambia de fase a lo largo del tiempo.
def animacion_seno(output_path=None, fps=20):
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 200)
    line, = ax.plot(x, np.sin(x), color='blue')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Onda Senoidal Animada')
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x + t)')
    ax.grid(True)

    def update(frame):
        phase = frame / 10
        line.set_ydata(np.sin(x + phase))
        return line,

    ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
    if output_path:
        writer = PillowWriter(fps=fps)
        ani.save(output_path, writer=writer)
        print(f"[INFO] Animación seno guardada en: {output_path}")
    plt.show()

# ====================================================================================
# 2. Puntos aleatorios moviéndose (ruido)
#    Objetivo: Simular partículas que se mueven aleatoriamente en el plano.
def puntos_aleatorios(n_points=50, steps=100, output_path=None, fps=20):
    fig, ax = plt.subplots()
    x = np.random.rand(n_points) * 3
    y = np.random.rand(n_points) * 3
    scatter = ax.scatter(x, y, color='blue')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_title('Puntos Aleatorios en Movimiento')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')

    def update(frame):
        nonlocal x, y
        x += (np.random.rand(n_points) - 0.5) * 0.1
        y += (np.random.rand(n_points) - 0.5) * 0.1
        scatter.set_offsets(np.c_[x, y])
        return scatter,

    ani = FuncAnimation(fig, update, frames=steps, interval=50, blit=True)
    if output_path:
        writer = PillowWriter(fps=fps)
        ani.save(output_path, writer=writer)
        print(f"[INFO] Animación puntos guardada en: {output_path}")
    plt.show()

# ====================================================================================
# 3. Círculo girando alrededor del origen
#    Objetivo: Animar un punto que describe un círculo, con trayectoria tipo "cola".
def circulo_girando(trail=True, output_path=None, fps=20):
    fig, ax = plt.subplots()
    t = np.linspace(0, 2 * np.pi, 200)
    x = np.cos(t)
    y = np.sin(t)

    line, = ax.plot([], [], color='blue')
    point, = ax.plot([], [], 'ro')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Círculo Girando')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')

    def init():
        line.set_data([], [])
        point.set_data([], [])
        return line, point

    def update(frame):
        if trail:
            line.set_data(x[:frame], y[:frame])
        else:
            line.set_data([], [])
        point.set_data(x[frame-1], y[frame-1])
        return line, point

    ani = FuncAnimation(fig, update, frames=len(t)+1,
                        init_func=init, interval=50, blit=True)
    if output_path:
        writer = PillowWriter(fps=fps)
        ani.save(output_path, writer=writer)
        print(f"[INFO] Animación círculo guardada en: {output_path}")
    plt.show()

# ====================================================================================
# 4. Visualización de evolución de datos desde CSV
#    Objetivo: Leer un CSV y animar cómo varía un valor por año para un país o región.
def animacion_evolucion_csv(csv_path, country_col, value_col, filter_country, output_path=None, fps=5):
    df = pd.read_csv(csv_path)
    df = df[df[country_col] == filter_country].sort_values('Year')
    years = df['Year'].values
    values = df[value_col].values

    fig, ax = plt.subplots()
    line, = ax.plot([], [], color='green')
    ax.set_xlim(years.min()-1, years.max()+1)
    ax.set_ylim(0, values.max()*1.1)
    ax.set_title(f'{value_col} en {filter_country} a lo largo de los años')
    ax.set_xlabel('Año')
    ax.set_ylabel(value_col)

    def init():
        line.set_data([], [])
        return line,

    def update(i):
        line.set_data(years[:i], values[:i])
        return line,

    ani = FuncAnimation(fig, update, frames=len(years), init_func=init, interval=500, blit=True)
    if output_path:
        writer = PillowWriter(fps=fps)
        ani.save(output_path, writer=writer)
        print(f"[INFO] Animación CSV guardada en: {output_path}")
    plt.show()

# ====================================================================================
# 5. Sistema planetario simple
#    Objetivo: Animar planetas girando alrededor de una estrella con diferentes radios y velocidades.
def sistema_planetario(planetas, output_path=None, fps=20):
    # planetas: lista de dicts {'r': radio_orbital, 'omega': angular_speed, 'color': color}
    fig, ax = plt.subplots()
    ax.set_xlim(-max(p['r'] for p in planetas)*1.2, max(p['r'] for p in planetas)*1.2)
    ax.set_ylim(-max(p['r'] for p in planetas)*1.2, max(p['r'] for p in planetas)*1.2)
    ax.set_aspect('equal')
    ax.set_title('Sistema Planetario Simple')

    artists = []
    for p in planetas:
        artist, = ax.plot([], [], 'o', color=p.get('color', 'blue'))
        artists.append(artist)

    def init():
        for art in artists:
            art.set_data([], [])
        return artists

    def update(frame):
        for idx, p in enumerate(planetas):
            theta = p['omega'] * frame
            x = p['r'] * np.cos(theta)
            y = p['r'] * np.sin(theta)
            artists[idx].set_data(x, y)
        return artists

    ani = FuncAnimation(fig, update, frames=360, init_func=init, interval=50, blit=True)
    if output_path:
        writer = PillowWriter(fps=fps)
        ani.save(output_path, writer=writer)
        print(f"[INFO] Animación planetaria guardada en: {output_path}")
    plt.show()

# ====================================================================================
# Ejemplo de uso si se ejecuta como script
if __name__ == '__main__':
    base_dir = r"C:/Users/Natalia/OneDrive/Attachments/pythonBootcamp/graficas"
    os.makedirs(base_dir, exist_ok=True)

    # 1.
    animacion_seno(output_path=os.path.join(base_dir, 'seno.gif'))
    # 2.
    puntos_aleatorios(output_path=os.path.join(base_dir, 'puntos_aleatorios.gif'))
    # 3.
    circulo_girando(output_path=os.path.join(base_dir, 'circulo.gif'))
    # 4. Asegúrate de reemplazar 'ruta.csv', 'Country', 'Value', 'Chile' con tus datos.
    # animacion_evolucion_csv(
    #     csv_path='ruta/a/tu/archivo.csv',
    #     country_col='Country',
    #     value_col='Value',
    #     filter_country='Chile',
    #     output_path=os.path.join(base_dir, 'evolucion.csv.gif')
    # )
    # 5.
    sistema_planetario(
        planetas=[
            {'r': 1, 'omega': 0.05, 'color': 'yellow'},
            {'r': 1.8, 'omega': 0.03, 'color': 'blue'},
            {'r': 2.5, 'omega': 0.02, 'color': 'red'}
        ],
        output_path=os.path.join(base_dir, 'planetario.gif')
    )
