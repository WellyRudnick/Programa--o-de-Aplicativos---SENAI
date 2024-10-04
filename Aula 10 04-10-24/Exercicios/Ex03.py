# Inicializa o vetor de poltronas com 50 elementos vazios
poltronas = [None] * 50

def vender_passagem(poltrona):
    poltrona = int(input("Digite o número da poltrona: "))
    if poltronas[poltrona - 1] is None:
        poltronas[poltrona - 1] = "Vendida"
        print(f"Passagem da poltrona {poltrona} vendida com sucesso!")
    else:
        print(f"A poltrona {poltrona} já está ocupada.")

def exibir_poltronas():
    for i, status in enumerate(poltronas):
        if status is None:
            #print(f"Poltrona {i + 1}: Livre")
        #else:
            print(f"Poltrona {i + 1}: {status}")

# Exemplo de uso
vender_passagem(poltronas)
exibir_poltronas()