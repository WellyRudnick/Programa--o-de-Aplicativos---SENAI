num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

menor = min(num1, num2)
maior = max(num1, num2)

for i in range(menor + 1, maior):
    print(i)