n = int(input("Digite um número inteiro positivo: "))
numero = 2
divisores = 0 # divisores é a variável contadora

while numero <= n-1:
    if n % numero == 0: # se n é divisível por numero
        divisores += 1
    numero += 1

if divisores == 0:
    print("É primo.")
elif divisores == 1:
    print("Não é primo. possui 1 divisor diferente de 1 e", n)
else:
    print("Não é primo. Possui", divisores, "divisores diferentes de 1 e", n)