import numpy as np
from scipy.special import factorial as fact

def mytan(angulo):
    somatorios = 30
    """ CALCULA O COSSENO """
    n = np.arange(somatorios)

    sinal = np.array(somatorios * [-1])
    sinal = sinal ** n

    x = np.array(somatorios * [angulo])
    x = x ** (2 * n)

    den = 2 * n
    fatorial = fact(den)

    cos = np.sum((sinal * x) / fatorial)

    """ CALCULA O SENO """
    sen = 1 - (cos ** 2)

    """ CALCULA A TANGENTE """
    tg = np.sqrt(sen) / cos
    return tg

def teste():
    rad = float(input("Digite o angulo: "))
    tg = mytan(rad)

    print(f"tg({rad}) = {tg}")

if __name__ == "__main__":
    teste()