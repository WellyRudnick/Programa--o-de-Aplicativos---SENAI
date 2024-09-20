def pop():
    popA = 80000
    popB = 200000
    anos = 0
    while popA < popB:
        popA += popA * 0.03
        popB += popB * 0.015
        anos += 1
    print("Serão necessários", anos, "anos para a população A ultrapassar a população B")    
    return anos

pop()