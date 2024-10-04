def jogo_da_velha():
    # Criar tabuleiro vazio
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Variável para controlar o jogador atual
    jogador_atual = "X"

    # Variável para controlar o número de jogadas
    jogadas = 0

    # Loop principal do jogo
    while True:
        # Imprimir tabuleiro
        imprimir_tabuleiro(tabuleiro)

        # Ler a posição do jogador atual
        linha = int(input(f"Jogador {jogador_atual} - Digite a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador_atual} - Digite a coluna (0-2): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] == " ":
            # Preencher a posição com o símbolo do jogador atual
            tabuleiro[linha][coluna] = jogador_atual

            # Verificar se alguém ganhou
            ganhador = verificar_ganhador(tabuleiro)
            if ganhador:
                imprimir_tabuleiro(tabuleiro)
                print(f"O jogador {ganhador} venceu!")
                break

            # Incrementar o número de jogadas
            jogadas += 1

            # Verificar se todas as posições foram preenchidas (empate)
            if jogadas == 9:
                imprimir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break

            # Trocar de jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")
            print("Posição inválida. Tente novamente.")
            print("Posição inválida. Tente novamente.")

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Função para verificar se alguém ganhou
def verificar_ganhador(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    # Se não houver ganhador
    return None

jogo_da_velha()
