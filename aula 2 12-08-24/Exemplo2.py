# fruta = input("Digite o nome de uma fruta: ")
# print("A fruta digitada foi",fruta)

codigo = int(input("Digite o codigo do funcionario: "))
nome = input("Digite o nome do funcionario: ")
salario = float(input("Informe o salario: "))
ativo = input("O funcionario está ativo?(S / N) ")

if ativo == "S" or ativo == "s":
    ativo = True
else:
    ativo = False

print('Codigo:', codigo)
print("Nome:", nome)
print("Salário: R$%.2f"% salario)
print("Ativo:", ativo)
