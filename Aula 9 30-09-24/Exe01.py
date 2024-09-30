n = int(input("Digite um número: "))
l = []

for i in range(1,n+1):
    l.append(i)
    for j in l:
        print(j, end=" ")
    print()

print("\n")

m = int(input("Digite um número: "))
k = []

for i in range(1,n+1):
    k.append(i)
    print(k)