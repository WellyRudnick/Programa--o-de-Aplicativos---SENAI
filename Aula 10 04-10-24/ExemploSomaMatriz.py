def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            num = int(input(f"{i+1}, {j+1}: "))
            mat[i].append(num)
    return mat


def ImprimirMatriz(mat):
    for linha in mat:
        for num in linha:
            print(num, end=" ")
        print()


def somaMatriz(mat1, mat2):
    tam = len(mat1)
    mat3soma = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3soma[i][j] = mat1[i][j] + mat2[i][j]
    return mat3soma


def multMatriz(mat1, mat2):
    tam = len(mat1)
    mat3mult = [[0 for j in range(tam)] for i in range(tam)]
    for i in range(tam):
        for j in range(tam):
            mat3mult[i][j] = mat1[i][j] * mat2[i][j]
    return mat3mult


n = int(input("Digite a dimensão da matriz: "))
mat1 = leMatriz(n)
mat2 = leMatriz(n)
print("Matriz 1:")
ImprimirMatriz(mat1)
print("Matriz 2:")
ImprimirMatriz(mat2)
mat3soma = somaMatriz(mat1, mat2)
print("Matriz 3 (soma):")
ImprimirMatriz(mat3soma)
mat3mult = multMatriz(mat1, mat2)
print("Matriz 3 (multiplicação):")
ImprimirMatriz(mat3mult)
