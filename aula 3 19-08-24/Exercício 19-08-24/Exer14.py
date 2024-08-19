numeros = []

# Solicita n números e os coloca numa matriz
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")

#Realiza a soma e a média dos números solicitados
soma = sum(numeros)
media = soma / len(numeros)
print("Soma:", soma)
print("Média:", media)
