n = int(input("Digite a quantidade de números: "))
anterior = int(input())

i = 1 # leu um número
ordenado = 0 # ordenado é a variavel indicadora

while (i < n) and (ordenado == 0):
    atual = int(input())
    i += 1 # leu mais um número
    if (atual <= anterior):
        ordenado += 1
    anterior = atual

if (ordenado == 0):
    print("Sequência está ordenada.")
else:
    print("Sequência não está ordenada.")