import numpy as np
import matplotlib.pyplot as plt
# x^2 + y^2 = 1
x = np.linspace(0, 1, 100)
y = np.sqrt(1 - x**2)
# Variavel auxiliar
size = 1000
# Pontos aleatorios no intervalo [0,1)
xdots = np.random.rand(size)
ydots = np.random.rand(size)
# Divide os pontos entre fora e dentro do 1/4 de circunferencia
outside = xdots**2 + ydots**2 > 1
inside = xdots**2 + ydots**2 <= 1
dots_outside = np.array([xdots[outside], ydots[outside]])
dots_inside = np.array([xdots[inside], ydots[inside]])
# Assumindo um número infinitesimal de pontos contidos no quadrado de lado 1,
# podemos afirmar que a área de uma figura contida no quadrado é aproximadamente
# igual à proporção da área dessa figura em relação à área do quadrado. Podemos
# interpretar como a proporção entre a quantidade de pontos contidos dentro da
# figura em relação à quantidade de pontos contida no quadrado
# Sabemos que a área do quadrado é l^2 e a área de 1/4 de circunferência é
# (pi*r^2)/4. Logo, se r = 1, pi = 4 * área de 1/4 de circunferencia
circle_area = (dots_inside.size / 2) / size
pi = 4 * circle_area
print("pi ~ {}, aproximando com {} pontos".format(pi, size))

plt.close("all")
plt.plot(dots_outside[0], dots_outside[1], "bo")
plt.plot(dots_inside[0], dots_inside[1], "ro")
plt.plot(x, y, "black", linewidth = 2)
plt.title("Grafico de 1/4 de circunferencia")
plt.xlabel("Raio")
plt.ylabel("Raio")
plt.grid()
plt.show()