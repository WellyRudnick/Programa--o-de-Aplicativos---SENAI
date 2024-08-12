notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >= 7.0:
    print("A media: %.1f - Aprovado"% mediafinal)
elif mediafinal >= 5:
    print("A media: %.1f - Exame"% mediafinal)
else:
    print("A Media: %.1f - Reprovado"% mediafinal)