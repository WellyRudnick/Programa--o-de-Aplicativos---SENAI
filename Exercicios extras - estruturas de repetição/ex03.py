def cadastro():
    nome = input("Digite seu nome: ")
    while len(nome) <= 3:
        print("Nome inválido, digite novamente")
        nome = input("Digite seu nome: ")

    idade = int(input("Digite sua idade: "))
    while idade < 0 and idade > 150:
        print("Idade invalida! Digite um valor maior que 0 e menor que 150")
        idade = int("Digite sua idade: ")

    salario = float(input("Digite seu salário: "))
    while salario < 0:
        print("Digite um valor maior que 0!")
        salario = float(input("Digite seu salário: "))

    sexo = input("Digite seu sexo (F/M): ")
    sexo = sexo.upper()
    while sexo != "F" or sexo != "M":
        print("Sexo inválido! Digite F ou M!")
        sexo = input("Digite seu sexo: ")

    estado_civil = input("Digite seu estado civil (s, c, v ou d): ")
    estado_civil = estado_civil.lower()
    while estado_civil != "s" or estado_civil != "c" or estado_civil != "v" or estado_civil != "d":
        print("Estado civil invalido!")
        estado_civil = input("Digite seu estado civil (s, c, v ou d): ")

    print("Cadastro realizado com sucesso!")


cadastro()
