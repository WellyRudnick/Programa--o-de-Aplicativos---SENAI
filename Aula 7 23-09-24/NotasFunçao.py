def leNotas(num):
    notas = []
    for i in range(num):
        dado = float(input("Digite a nota do aluno: "))
        notas.append(dado)
    return notas

def calculaMedia(notas):
    soma = 0
    for i in range(len(notas)):
        soma += notas[i]
    return (soma/len(notas))

n = int(input("Digite a número de notas: "))
notas = leNotas(n)
print("As notas são:", notas)
media = calculaMedia(notas)
print(f"A média das notas é {media:.1f}")

