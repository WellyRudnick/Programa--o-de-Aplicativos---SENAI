notas = []

n = int(input("Digite a quantidade de nostas: "))

for i in range(n):
    dado = float(input("Digite a nota: "))
    notas.append(dado)

print(notas)

soma = 0
for i in range(len(notas)):
    soma += notas[i]

media = soma / len(notas)

print(f"A média das notas é {media:.2f}")