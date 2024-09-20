impar = []
par = []

for i in range(10):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f"foram digitados {len(par)} números pares")
print(f"foram digitados {len(impar)} números ímpares")