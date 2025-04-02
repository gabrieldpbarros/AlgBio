name = input("Insira o nome do usuario: ")
height = float(input("Insira sua altura: "))
weight = int(input("Insira seu peso: "))
IMC = weight / (height**2)

print(f"{name} tem {weight} quilos e a altura de {height} e portanto o IMC é de {IMC:.1f}")