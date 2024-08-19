#Função para verificar o MDC de 2 numeros
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

#Chama a função
resultado = mdc(num1, num2)
print("MDC: ", resultado)
