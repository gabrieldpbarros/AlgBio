#função para remover todos os elementos duplicados em uma lista
lista = []
for i in range(5):
    numero = int(input(f"Palavra {i+1}:"))
    lista.insert(i,numero)
print(lista)

contador = 0
lista2 = lista[:]
for i in range(5):
    num = lista[i]
    contador = lista.count(num)
    if contador > 1 :
        lista2.pop(i)
print(lista2)