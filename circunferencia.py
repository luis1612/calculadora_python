import numpy as np
import matplotlib.pyplot as plt


# Se sefine una función que tome ekl rago y el incremento para el loop
def deg_range(start, end, step):
    while start <= end:
        yield start
        start += step


# Son los puntos que se usaran como parejas (x,y) en la gráfica
x = []
y = []

# Se almacenan los valores en el array
for i in deg_range(0, 2 * np.pi, np.pi / 180):
    x.append(np.cos(i))
    y.append(np.sin(i))

plt.plot(x, y, "b--")
plt.show()
