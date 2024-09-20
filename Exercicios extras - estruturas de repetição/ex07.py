maior = 0
for i in range(5):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
print('O maior número digitado foi:', maior)