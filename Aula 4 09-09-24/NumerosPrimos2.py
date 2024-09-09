n = int(input("Digite um número inteiro positivo: "))
if n <= 1:
    print("O número", n, "não é primo.")
    exit()

numero = 2
primo = True  # primo é a variavel indicadora

while (numero <= n-1):
    if (n % numero == 0):  # se n é divisível por numero
        primo = False
        break
    numero += 1

if (primo):
    print("O número", n, "é primo.")
else:
    print("O número", n, "não é primo.")
