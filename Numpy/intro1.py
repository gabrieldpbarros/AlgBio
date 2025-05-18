""" EX DE OPERACAO SEM NUMPY: """
matrix = [[1, 2, 3], # Estou definindo matrizes assim pra ficar mais fácil de visualizar,
          [4, 5, 6], # mas geralmente são definidas em uma linha.
          [3, 6, 7]]
# Matriz definida na mesma linha: m = [[1,2,3], [4,5,6], [3,6,7]]

matrix3x = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
# Objetivo = 3 * matrix
print("OPERACAO SEM NP:")
for i in range(3):
    for j in range(3):
        matrix3x[i][j] = 3 * matrix[i][j] # Coloca o resultado da operação na matriz "matrix3x"
        print(matrix3x[i][j], end=' ')
    print() # Nova linha
print()
# Temos um código muito ineficiente e extenso para uma operação simples como multiplicar
# um escalar por uma matriz.

""" NUMPY """
# Toda biblioteca precisa ser importada explicitamente, como feito adiante.
# Qualquer função pertencente a uma biblioteca externa tem o formato
# "nome_da_biblioteca.função...". Para otimizar um pouco a escrita do código,
# geralmente importamos a biblioteca da seguinte forma:
# "import [biblioteca] as [nome_qualquer]".
# Por exemplo, para a biblioteca math, podemos fazer o seguinte:
# import math as m
# a fim de, em vez de precisar escrever "math" antes de qualquer função da
# biblioteca, podermos escrever apenas "m".
import numpy as np # OBS: SEMPRE NA PRIMEIRA LINHA (aqui é um exemplo, então estou quebrando a regra kkkk)

# Quais as vantagens?
# Python é uma linguagem ineficiente para operações matriciais,
# funções mais sofisticadas e outras operações. A biblioteca
# auxilia na realização dessas operações de forma mais eficiente.

""" Mesma operação feita no início, mas agora utilizando NumPy: """
matrixNP = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [3, 6, 7]])
print("OPERACAO COM NP:")
print(3 * matrixNP)
print()

# A parte central do NumPy é o "ndarray", matriz alocada em espaços
# contínuos de memória.
# Podemos criar um ndarray da seguinte forma:
ndarray = np.array(matrix) # Lembrando de "matrix", declarada no começo do arquivo
# EX:
m = np.array([[1, 2, 3], # Converte a lista de listas em uma matriz NumPy
              [4, 5, 6],
              [3, 6, 7]])
print("NDARRAYS:")
print(m[0,0]) # SINTAXE = variavel[linha, coluna]; OUTPUT = 1
print(m[-1,1]) # OUTPUT = 6 (-1 indica último índice)

qtd_de_elementos = m.size # OUTPUT = 9
forma_da_matriz = m.shape # OUTPUT = (3,3); Matriz 3 por 3
dimensao = m.ndim # OUTPUT = 2; Indica a dimensão da matriz
tipo_da_variavel = m.dtype # OUTPUT = dtype('int64'); Indica o tipo das variáveis da matriz
print(qtd_de_elementos)
print(forma_da_matriz)
print(dimensao)
print(tipo_da_variavel)
print()

""" Criando um vetor com um loop """
print("LOOPS:")
v_loop = np.arange(0, 10, 2) # SINTAXE = np.arrange(primeiro_elemento, último_elemento, passo);
                             # OBS: a ideia é a mesma do for loop (intervalo = [primeiro_elemento, ultimo_elemento)).
print(v_loop) # OUTPUT = [0 2 4 6 8]

v_nulo = np.zeros(5) # SINTAXE = np.zeros(formato); Se quiser fazer um array nulo, basta seguir o exemplo
                     # feito. Agora, se for uma matriz, deve ser feito da forma np.zeros((linha, coluna))
print(v_nulo)

matriz_nula = np.zeros((2,2)) # Matriz nula 2x2
print(matriz_nula)

v_um = np.ones(5) # Mesma ideia do np.zeros(), mas faz um vetor que contém apenas elementos "1".
print(v_um) # OUTPUT = [1. 1. 1. 1. 1.]

# Outra forma semelhante às funções np.zeros() e np.ones() é a seguinte:
vt = np.arange(5) # Vetor = [0 1 2 3 4]
v_nulo2 = np.zeros_like(vt)
v_um2 = np.ones_like(vt)
print(v_nulo2) # OUTPUT = [0 0 0 0 0]
print(v_um2) # OUTPUT = [1 1 1 1 1]
# A diferença está nos argumentos da função: zeros/ones_like criam um vetor com mesmo formato do vetor
# utilizado como argumento para a função, que é "vt". Além disso, a saída não possui pontos após cada
# número do vetor.

# Se quisermos um vetor/matriz que contenha apenas determinado número, basta multiplicar esse escalar
# pelo vetor/matriz do np.ones()
""" EX: Quero um vetor que tenha apenas números "6" """
v_seis = 6 * np.ones(5)
print(v_seis) # OUTPUT = [6. 6. 6. 6. 6.]

espacados = np.linspace(0, 1, 5) # SINTAXE = np.linspace(valor_inicial, valor_final, tamanho); Cria um vetor que
                                 # contém N elementos igualmente espaçados entre um valor_incial e um valor_final,
                                 # sendo N igual ao tamanho do vetor. (intervalo = [valor_inicial, valor_final])
print(espacados) # OUTPUT = [0. 0.25 0.5 0.75 1.]; OBS = 5 elementos igualmente espaçados entre 0 e 1

aleatorios = np.random.randint(0, 10, (3,3)) # SINTAXE = np.random.randint(valor_min, valor_max, formato)
print(aleatorios) # OUTPUT = matriz 3x3 com números aleatórios entre 0 e 9 (intervalo = [0,10))
print()

""" Tipos de variáveis """
# Semelhante à ideia de tipos em C, mas com maior flexibilidade.
# Para conhecer alguns tipos NumPy, consultar a tabela nos slides da aula 1 de NumPy.
# Exemplo de manipulação do tipo das variáveis de um vetor:
print("TIPOS:")
tipo = np.ones_like(vt, dtype='int8')
print(tipo.dtype) # OUTPUT = int8
tipo = np.ones_like(vt, dtype=np.int8) # Mesma coisa do exemplo imediatamente acima, somente com sintaxe diferente
print(tipo.dtype) # OUTPUT = int8
tipo = tipo.astype('int64')
print(tipo.dtype) # OUTPUT = int64
print()

""" Operações com matrizes """
m = np.array([[1, 2],
              [3, 4]])
n = np.array([[5, 6],
              [7, 8]])

# Operações elemento a elemento
print("ELEMENTO A ELEMENTO:")
soma = m + n
sub = m - n 
mult = m * n
div = n / m
div_int = n // m # Divisão inteira (EX: 1 // 2 = 0)
pot = m ** n # Eleva o elemento m[i][j] à potência n[i][j]
print(soma)
print(sub)
print(mult)
print(div)
print(div_int)
print(pot)
print()

# Operações com escalares
print("ESCALAR:")
soma_esc = 10 + m
sub_esc = 7 - m
mult_esc = 5 * m
div_esc = m / 2
print(soma_esc)
print(sub_esc)
print(mult_esc)
print(div_esc)
print()

# Multiplicação de matrizes
print("MULTIPLICACAO DE MATRIZES:")
mult_matrix = np.dot(m, n)
print(mult_matrix)
print("\n")

""" EXEMPLO DO NUMERO DE EULER """
from scipy.special import factorial # O fatorial do NumPy não funciona por alguma razão,
                                    # então usamos o fatorial da biblioteca scipy.special.
def euler(x):
    numerador = x * np.ones(6)
    denominador = factorial(np.arange(6))
    potencias = np.arange(6)

    euler = sum((numerador ** potencias) / denominador)
    return euler

print("EXEMPLO FINAL SLIDES 1:")
pot_euler = int(input("Insira a potencia do numero de Euler: "))
e = euler(pot_euler)
print(f"e^{pot_euler} = {e}")
print()
# TE 4M0 SARINHA <3