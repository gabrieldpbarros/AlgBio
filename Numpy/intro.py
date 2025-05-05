# EX DE OPERACAO SEM NP
matrix = [[1, 2, 3], # Estou definindo matrizes assim pra ficar mais fácil de visualizar,
          [4, 5, 6], # mas geralmente são definidas em uma linha.
          [3, 6, 7]]
# Matriz definida na mesma linha: m = [[1,2,3], [4,5,6], [3,6,7]]

matrix3x = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# Toda biblioteca precisa ser importada explicitamente, como feito adiante.
# Qualquer função pertencente a uma biblioteca externa tem o formato
# "nome_da_biblioteca.função...". Para otimizar um pouco a escrita do código,
# geralmente importamos a biblioteca da seguinte forma:
# "import [biblioteca] as [nome_qualquer]"".
# Por exemplo, para a biblioteca math, podemos fazer o seguinte:
# import math as m
# a fim de, em vez de precisar escrever "math" antes de qualquer função da
# biblioteca, podermos escrever apenas "m".
import numpy as np # OBS: SEMPRE NA PRIMEIRA LINHA (aqui é um exemplo, então estou quebrando a regra kkkk)

# Quais as vantagens?
# Python é uma linguagem ineficiente para operações matriciais,
# funções mais sofisticadas e outras operações. A biblioteca
# auxilia na realização dessas operações de forma mais eficiente.

# A parte central do NumPy é o "ndarray", matriz alocada em espaços
# contínuos de memória.
# EX:
m = np.array([[1, 2, 3], # Converte a lista de listas em uma matriz NumPy
              [4, 5, 6],
              [3, 6, 7]])
print(m[0,0]) # SINTAXE = variavel[linha, coluna]; OUTPUT = 1
print(m[-1,1]) # OUTPUT = 6 (-1 indica último índice)

qtd_de_elementos = m.size # OUTPUT = 9
forma_da_matriz = m.shape # OUTPUT = (3,3); Matriz 3 por 3
dimensao = m.ndim # OUTPUT = 2; Indica a dimensão da matriz
tipo_da_variavel = m.dtype # OUTPUT = dtype('int64'); Indica o tipo das variáveis da matriz

# Criando um vetor com um loop
v_loop = np.arrange(0, 10, 2) # SINTAXE = np.arrange(primeiro elemento, último elemento do loop, passo);
                              # OBS: a ideia é a mesma do for loop.
print(v_loop) # OUTPUT = array([0, 2, 4, 6, 8])

v_nula = np.zeros(5) # SINTAXE = np.zeros(formato); Se quiser fazer um array nulo, basta seguir o exemplo
                     # feito. Agora, se for uma matriz, deve ser feito da forma np.zeros((linha, coluna))

matriz_nula = np.zeros((2,2)) # Matriz nula 2x2

v_um = np.ones(5) # Mesma ideia do np.zeros(), mas faz um vetor que contém apenas elementos "1".
print(v_um) # OUTPUT = array([1, 1, 1, 1, 1])

# Se quisermos um vetor/matriz que contenha apenas determinado número, basta multiplicar esse escalar
# pelo vetor/matriz do np.ones()
# EX: Quero um vetor que tenha apenas números "6"
v_seis = 6 * np.ones(5)
print(v_seis) # OUTPUT = array([6, 6, 6, 6, 6])

# Operações
m = np.array([[1, 2],
              [3, 4]])
n = np.array([[5, 6],
              [7, 8]])