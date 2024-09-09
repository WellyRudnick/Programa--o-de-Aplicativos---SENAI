n = int(input("Digite a quantidade de números: "))
anterior = int(input())

i = 1 # leu um número
ordenado = True # ordenado é a variavel indicadora

while (i < n) and (ordenado):
    atual = int(input())
    i += 1 # leu mais um número
    if (atual < anterior):
        ordenado = False
    anterior = atual

if (ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")