contador = 0
minha_lista = []

def incrementar_contador():
    global contador
    contador += 1
    return contador

def exibir_contador():
    global contador
    print(contador)

def adicionar_na_lista(item, lista):
    global minha_lista
    n = int(input("Digite o número de itens a serem adicionados: "))
    for i in range(n):
        item = input(f"Digite o {i+1}° item a ser adicionado: ")
        lista.append(item)
    return minha_lista

def exibir_lista(minha_lista):
    print(f"Itens da lista: {minha_lista}")

def main():
    global minha_lista
    adicionar_na_lista(None, minha_lista)
    exibir_lista(minha_lista)
    incrementar_contador()
    print(f"Contador atualizado: {contador}")
    incrementar_contador()
    print(f"Contador atualizado: {contador}")
    print(f"Valor atual do contador: {contador}")

main()
