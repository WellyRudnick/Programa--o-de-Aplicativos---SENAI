# Criando a matriz para armazenar os tempos
tempos = []

# Loop para obter os tempos de cada piloto
for i in range(4):
    piloto = []
    print(f"Informe os tempos do piloto {i+1}:")
    for j in range(4):
        tempo = float(input(f"Volta {j+1}: "))
        piloto.append(tempo)
    tempos.append(piloto)

# Imprimindo os tempos
print("Tempos dos pilotos:")
for i in range(4):
    print(f"Piloto {i+1}: {tempos[i]}")