n = int(input("Quantos numeros deseja digitar? "))
if n < 0 or n > 1000:
    print("Digite um número entre 0 e 1000")
    exit()
conjunto = []

for i in range(n):
    conjunto.append(int(input(f"Digite o {i+1}º número: ")))

print(f"\nO maior número digitado foi {max(conjunto)}\nO menor número digitado foi {min(conjunto)}\nA soma dos números digitados foi {sum(conjunto)}")
