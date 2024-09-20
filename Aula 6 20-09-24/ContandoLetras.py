n = input("Digite uma palavra: ")
n = n.upper()
dicionario = {}
for i in n:
    if i in dicionario:
        dicionario[i] += 1
    else:
        dicionario[i] = 1

print()
print(f"A letra que mais repetiu é {max(dicionario, key=dicionario.get)} e repetiu {dicionario[max(dicionario, key=dicionario.get)]} vezes")
