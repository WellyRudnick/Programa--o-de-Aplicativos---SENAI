import random


def jogo():

    j1 = int(input("Jogador 1, escolha: 0 - Pedra, 1 - Papel, 2 - Tesoura: "))
    escolhas = ["Pedra", "Papel", "Tesoura"]
    j2 = random.randint(0, 2)

    if j1 < 0 or j1 > 2:
        print("Escolha inválida!")
        jogo()

    print("Jogador 1 escolheu: ", escolhas[j1])
    print("Jogador 2 escolheu: ", escolhas[j2])

    if j1 == j2:
        print("Empate!")
    elif j1 == 0 and j2 == 1:
        print("Jogador 2 venceu!")
    elif j1 == 0 and j2 == 2:
        print("Jogador 1 venceu!")
    elif j1 == 1 and j2 == 0:
        print("Jogador 1 venceu!")
    elif j1 == 1 and j2 == 2:
        print("Jogador 2 venceu!")
    elif j1 == 2 and j2 == 0:
        print("Jogador 2 venceu!")
    elif j1 == 2 and j2 == 1:
        print("Jogador 1 venceu!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente == "s" or jogar_novamente == "S":
        jogo()
    else:
        print("Fim do jogo!")
        

jogo()