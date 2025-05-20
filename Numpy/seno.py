import numpy as np
from scipy.special import factorial

# o codigo está errado

x = int(input("ANGULO: "))
n = np.arange(30)
b = 2*n + 1
bb = factorial(n)
a = x ** b
a[1:-1:2] *= -1
c = a/bb
print(f"n = {n}\n b = {b}\n bb = {bb}\n a = {a}")
print(f"sen = {c.sum()}, {np.sin(1)}")