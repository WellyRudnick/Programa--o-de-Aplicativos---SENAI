def pop():
    popA = int(input("Digite a população da cidade A: "))
    popB = int(input("Digite a população da cidade B: "))
    txA = float(input("Digite a taxa de crescimento da cidade A: "))
    while txA <= 0:
        print("Digite um valor maior que 0!")
        txA = float(input("Digite a taxa de crescimento da cidade A: "))
    txB = float(input("Digite a taxa de crescimento da cidade B: "))
    while txB <= 0:
        print("Digite um valor maior que 0!")
        txB = float(input("Digite a taxa de crescimento da cidade B: "))
    anos = 0
    while popA < popB:
        popA += popA * (txA / 100)
        popB += popB * (txB / 100)
        anos += 1
    print("Serão necessários", anos, "anos para a população A ultrapassar a população B")
    return anos


pop()
