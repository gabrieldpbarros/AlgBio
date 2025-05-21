import numpy as np

""" OPERAÇÕES MATRICIAIS PT.2 """
print("OPERACOES MATRICIAIS")
mat = np.random.randint(0, 10, (2, 3)) # Matriz 2x3 aleatória
mat_invertivel = np.random.randint(0, 10, (2, 2))
mat_inv = np.linalg.inv(mat_invertivel) # Matriz inversa
det = np.linalg.det(mat_invertivel) # Determinante da matriz
mat_trans = mat.T # Matriz transposta; ALTERNATIVA: mat.transpose()
print("Matriz aleatoria:\n{}".format(mat))
print("Matriz quadrada aleatoria:\n{}".format(mat_invertivel))
print("Matriz inversa:\n{}".format(mat_inv))
print("Determinante da matriz = {}".format(det))
print("Matriz transposta:\n{}\n".format(mat_trans))

""" EXTRAINDO INFORMAÇÕES DA MATRIZ """
# Eixo 0 = segue as linhas
# Eixo 1 = segue as colunas
print("INFORMACOES DA MATRIZ")
max_geral = mat.max() # total
max_por_lin = mat.max(1) # colunas
max_por_col = mat.max(0) # linhas
soma_total = mat.sum() # total
soma_coluna = mat.sum(1) # colunas
soma_linha = mat.sum(0) # linhas
soma_cumulativa = mat.cumsum() # Imprime a quantidade de valores da matriz, somando
                               # o próximo a cada valor imprimido
media_geral = mat.mean() # media geral
media_col = mat.mean(1) # media de cada coluna
media_lin = mat.mean(0) # media de cada linha
des_pad = mat.std() # desvio padrao geral
dp_col = mat.std(1) # desvio padrao de cada coluna
dp_lin = mat.std(0) # desvio padrao de cada linha
print("Maximos:")
print("Maior valor da matriz = {}".format(max_geral))
print("Maior valor de cada coluna = {}".format(max_por_col))
print("Maior valor de cada linha = {}".format(max_por_lin))
print("Somatorios:")
print("Soma de todos os elementos = {}".format(soma_total))
print("Soma dos valores de cada coluna = {}".format(soma_coluna))
print("Soma dos valores de cada linha = {}".format(soma_linha))
print("Soma cumulativa = {}".format(soma_cumulativa))
print("Medias:")
print("Media total = {}".format(media_geral))
print("Media de cada coluna = {}".format(media_col))
print("Media de cada linha = {}".format(media_lin))
print("Desvios padrao:")
print("Desvio padrao total = {}".format(des_pad))
print("Desvio padrao de cada coluna = {}".format(dp_col))
print("Desvio padrao de cada linha = {}".format(dp_lin))