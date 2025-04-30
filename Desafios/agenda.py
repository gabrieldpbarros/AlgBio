qtd = int(input("Digite a quantidade de contatos: "))
agenda = [{} for i in range(qtd)]

for i in range(qtd):
    agenda[i]["nome"] = input("Digite o nome do contato: ")
    agenda[i]["tel"] = input("Digite o telefone do contato: ")
    agenda[i]["CPF"] = input("Digite o CPF do contato: ")
    print()

for i in range(qtd):
    print(f"[Contato {i + 1}]:")
    for j, k in agenda[i].items():
        print(f"{j} => {k}")
    print()