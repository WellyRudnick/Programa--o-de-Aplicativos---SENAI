tempos = []

for i in range(4):
    piloto = []
    print(f"Informe os tempos do piloto {i+1}:")
    for j in range(4):
        tempo = float(input(f"Volta {j+1}: "))
        piloto.append(tempo)
    tempos.append(piloto)

print("Tempos dos pilotos:")

for i in range(4):
    print(f"Piloto {i+1}:")
    for j in range(4):
        tempo = tempos[i][j]
        minutos = int(tempo)
        segundos = (tempo - minutos) * 60
        print(f"  {minutos}m {segundos:.0f}s")

        #piloto 1: 
         #   1m0s