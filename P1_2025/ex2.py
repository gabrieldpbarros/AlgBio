def maiores25(list, size):
    maior_25 = []
    for i in range(size):
        if (list[i]["idade"] > 25):
            maior_25.append(list[i]["nome"])

    return maior_25

def teste():
    lista = []
    qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
    for i in range(qtd_pessoas):
        aux = {}
        aux["nome"] = input("Digite o nome da pessoa {}: ".format(i + 1))
        aux["idade"] = int(input("Digite sua idade: "))
        aux["cidade"] = input("Digite sua cidade: ")
        lista.append(aux)

    lista_nova = maiores25(lista, qtd_pessoas)
    print(f"Pessoas com mais de 25 anos: {lista_nova}")
    
if __name__ == "__main__":
    teste()