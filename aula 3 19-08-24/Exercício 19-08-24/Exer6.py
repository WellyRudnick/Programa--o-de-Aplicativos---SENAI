#Realiza a conversão de km para metros
def converter_quilometros_para_metros(quilometros):
    metros = quilometros * 1000
    return metros

#Solicita um valor em km e chama a função para converter em metros
try:
    quilometros = float(input("Digite a distância em quilômetros:"))
    metros = converter_quilometros_para_metros(quilometros)
    print("metros: ", metros)

except ValueError:
    print("Entrada inválida!")
