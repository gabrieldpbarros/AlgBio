frutas = {"maca": 10,
          "banana": 4,
          "uva": 15,
          "goiaba": 3}
compras = {"maca": 3,
           "banana": 2,
           "uva": 1,
           "goiaba": 5}

carrinho = 0

for i in frutas.keys():
    carrinho += frutas[i] * compras[i]

chaves_a_remover = []
for fruta, preco in frutas.items():
    if preco > 5:
        chaves_a_remover.append(fruta)

for fruta in chaves_a_remover:
    frutas.pop(fruta) # ALTERNATIVA: del frutas[fruta]

print("Custo total =", carrinho)
print("Tabela de precos atualizada =", frutas)