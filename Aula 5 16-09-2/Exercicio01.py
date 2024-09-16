texto = input("Digite um texto: ")
texto = texto.lower().replace(" ", "")
inversa = texto[::-1]

print(texto)
print(inversa)

if texto == inversa:
    print("O texto '", texto, "' é palíndromo")
else:
    print("O texto '", texto, "' não é palíndromo")
