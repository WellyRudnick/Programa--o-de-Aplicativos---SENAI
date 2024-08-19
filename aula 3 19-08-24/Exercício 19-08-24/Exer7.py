#Funcão para saber qual foi o maior e o menor numero digitado
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento
    return maior, menor


lista = list()
i = 1

#loop para adicionar um número a uma matriz
while i <= 10:
    elem = int(input("Digite um elemento da lista: "))
    lista.append(elem)
    i += 1
    print(lista)

#chama a função e printa o maior e o menor número digitado
maior, menor = maior_menor(lista)
print("Maior:", maior)
print("Menor:", menor)
