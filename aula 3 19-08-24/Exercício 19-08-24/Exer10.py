#Realiza a função para retornar o ultimo número digitado
def obter_ultimo_elemento(lista):
    if lista:
        return lista[-1]
    else:
        return None


lista = list()
i = 1

#Solicita números para uma lista
while i <= 5:
    elem = int(input("Digite um elemento da lista: "))
    lista.append(elem)
    i+=1  

#printa a matriz e mostra o ultimo número digitado
print(lista)  
ultimo_elemento = obter_ultimo_elemento(lista)  
print("Último elemento da lista:", ultimo_elemento)
