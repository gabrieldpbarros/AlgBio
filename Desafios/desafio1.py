import random as r

key = r.randint(1, 25)
txt_original = input("Digite o texto a ser criptografado: ").lower()

print(key)
for letter in txt_original:
    ascii = ord(letter)
    if 96 < ascii < 123:
        if ascii + key > 122:
            dif = key - (122 - ascii)
            cypher = chr(96 + dif)
        else:
            cypher = chr(ord(letter) + key)

        print(f"{cypher}", end="")

    else:
        print(f"{letter}", end="")

print()
