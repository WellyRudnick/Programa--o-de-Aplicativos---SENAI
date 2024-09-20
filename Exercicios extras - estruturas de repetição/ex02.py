def login():
    while True:
        user = input("Digite o nome de usuário: ")
        password = input("Digite uma senha: ")
        if user != password:
            print("Usuário cadastrado com sucesso!")
        else:
            print("\nNome de usuário e senha não podem ser iguais!")
            login()
        break

login()