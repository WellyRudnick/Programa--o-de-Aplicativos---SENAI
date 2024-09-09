n = int(input("Digite a quantidade de números: "))
anterior = int(input())

ordenado = True  # ordenado é a variavel indicadora

for i in range(n-1):
    atual = int(input())
    i += 1  # leu mais um número
    if atual < anterior:
        ordenado = False
        break
    anterior = atual

if ordenado:
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
