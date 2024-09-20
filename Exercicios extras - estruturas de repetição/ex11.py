num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma = [num1, num2]

menor = min(num1, num2)
maior = max(num1, num2)

for i in range(menor + 1, maior):
    print(i)
    soma.append(i)
print('A soma dos números entre', num1, 'e', num2, 'é:', sum(soma))