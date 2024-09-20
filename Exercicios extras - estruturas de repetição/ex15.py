def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a + b
    return sequence

# Solicita ao usuário o valor de n
n = int(input("Digite o valor de n: "))

# Gera e imprime a série de Fibonacci até o n-ésimo termo
fib_sequence = fibonacci(n)
print(f"A série de Fibonacci até o {n}-ésimo termo é: {fib_sequence}")