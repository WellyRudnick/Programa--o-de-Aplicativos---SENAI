n = int(input("Quantos numeros deseja digitar? "))
conjunto = []

for i in range(n):
    conjunto.append(int(input(f"Digite o {i+1}º número: ")))

print(f"O maior número digitado foi {max(conjunto)}")
print(f"O menor número digitado foi {min(conjunto)}")
print(f"A soma dos números digitados foi {sum(conjunto)}")