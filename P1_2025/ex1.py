comp = 1

while(comp):
    person = {}
    person["name"] = input("Insira seu nome: ")
    person["age"] = int(input("Digite sua idade: "))
    person["glicemy"] = float(input("Digite sua glicemia: "))
    person["IMC"] = float(input("Digite seu IMC: "))

    if (person["glicemy"] < 100 and person["IMC"] < 25):
        print(f"{person["name"]} tem baixo risco de diabetes.")
    elif (100 <= person["glicemy"] <= 125 and 25 <= person["IMC"] <= 30):
        print(f"{person["name"]} tem risco moderado de diabetes.")
    else:
        print(f"{person["name"]} tem alto risco de diabetes.")
    
    comp = int(input("Continuar lendo? (Digite 1 ou 0): "))
    while (comp != 1 and comp != 0):
        print("ERRO, digite um valor correto.")
        comp = int(input("Continuar lendo? (Digite 1 ou 0): "))