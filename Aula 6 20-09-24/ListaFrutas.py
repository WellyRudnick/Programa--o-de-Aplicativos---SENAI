frutas = "maçã", "banana", "laranja"
precos = {0: 5, 1: 2.5, 2: 3}

for i in frutas:
    print(f"O preço da {i} é R$ {precos[frutas.index(i)]:.2f}")
