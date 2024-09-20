def calcular_fatorial(n):
    if n < 0:
        print("Fatorial não definido para números negativos.")
        exit()
    fatorial = 1
    sequencia = ""
    for i in range(n, 0, -1):
        fatorial *= i
        sequencia += f"{i} x " if i > 1 else f"{i} = {fatorial}"
    return fatorial, sequencia


numero = int(input("Digite um número inteiro: "))
resultado, sequencia = calcular_fatorial(numero)
print(f"{numero}! = {sequencia}")
