quant = int(input("Digite a quantidade de números: "))
num = []

for i in range(quant):
    num.append(int(input("Digite o número: ")))

if num[i] == num[i  - 1]:
    print("Há números adjacentes iguais.")
else:
    print("Não há números adjacentes iguais.")
