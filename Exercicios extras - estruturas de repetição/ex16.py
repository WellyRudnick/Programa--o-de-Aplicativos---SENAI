# Inicializa os dois primeiros números da série de Fibonacci
a, b = 0, 1

# Enquanto o valor de 'a' for menor ou igual a 500, continue gerando a série
while a <= 500:
    print(a, end=', ')
    a, b = b, a + b