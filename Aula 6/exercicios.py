import random as r

def factorial(number):
    mult = 1
    for i in range(number):
        mult *= number - i

    print(mult)

def maxnum(*list):
    return max(list[0])

def multiple(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        print("True.")
    else:
        print("False.")

def calc(op, n1, n2):
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 // n2)
    else:
        print("Operacao invalida.")

def maiorPalavra(*list): # incompleto
    print("a")

def __main__():
    n = int(input("Fatorial: "))
    factorial(n)

    size = int(input("Tamanho da tupla: "))
    max_list = []
    for i in range(size):
        max_list.append(r.randint(1, 1000))

    print(f"Original = ", max_list)
    print(f"Maior numero = ", maxnum(max_list))

    n, m = input("Digite dois numeros: ").split()
    multiple(int(n), int(m))

    op, number1, number2 = input("Digite a operacao e numeros respectivamente: ").split()
    calc(op, int(number1), int(number2))

__main__()