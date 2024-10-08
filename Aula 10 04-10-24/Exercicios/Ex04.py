tempos = []

for i in range(4):
    piloto = []
    print(f"Informe os tempos do piloto {i+1}:")
    for j in range(4):
        minutos = int(input(f"Volta {j+1} - Minutos: "))
        segundos = int(input(f"Volta {j+1} - Segundos: "))
        tempo = minutos + segundos / 60
        piloto.append(tempo)
    tempos.append(piloto)

print("Tempos dos pilotos:")

for i in range(4):
    print(f"Piloto {i+1}:")
    for j in range(4):
        tempo = tempos[i][j]
        minutos = int(tempo)
        segundos = (tempo - minutos) * 60
        print(f"  {minutos}m 0{segundos:.0f}s" if segundos < 10 else f"  {minutos}m {segundos:.0f}s")
