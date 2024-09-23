def quant(n):
    quant = len(str(n))
    return quant

n = int(input("Digite um número: "))
quantidade = quant(n)
print(f"O número {n} tem {quantidade} dígitos.")
