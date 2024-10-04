matriz = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}][{j + 1}]: "))


contador = 0
for i in range(10):
    for j in range(10):
        if matriz[i][j] != 0:
            contador += 1

print(f"Número de posições não nulas na matriz: {contador}")
