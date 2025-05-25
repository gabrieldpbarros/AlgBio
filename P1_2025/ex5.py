import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6.28, 100)
ysen = np.sin(x)
ycos = np.cos(x)

plt.close("all")
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, ysen, color="green", label=f"f(x) = sen(x)")
plt.title("Função seno")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x, ycos, color="blue", label=f"g(x) = cos(x)")
plt.title("Função cosseno")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.legend()
plt.grid()

plt.show()