txt_original = input("Digite o texto a ser criptografado: ").lower()

for key in range(25):
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

print()