notas = [8.0, 5.5, 9.3, 0.5, 3.1]
print(notas[1:4])

print("\n##################################\n")

print(len(notas))

print("\n##################################\n")

for i in range(len(notas)):
    print(notas[i])

print("\n##################################\n")

for i in notas:
    print(i)

print("\n##################################\n")

notas.append(9.5)
print(notas)

print("\n##################################\n")

notas2 = []
n = int(input("Entre com o número de notas: "))

for i in range(n):
    dado = float(input(f"Entre com a {i+1}ª nota: "))
    notas2.append(dado)
print(notas2)

# 
#for i in notas2:
#    print(f"Nota: {i}")

print("\n##################################\n")

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

x = lista2 + lista1
print(x)

print("\n##################################\n")

y = [1, 2, 3,]
z = 4*y
print(z)

print("\n##################################\n")

w = [40, 30, 10, 20]
w.insert(1, 99)
print(w)

print("\n##################################\n")

t = [40, 99, 10, 20]
print(t)

del t[1]
print(t)

t.remove(20)
print(t)

print("\n##################################\n")

u = [40, 99, 10, 20, 13, 20, 14]
r = u.count(20)
print(r)

print("\n##################################\n")

p = [0 for i in range(5)]
print(p)

q = [2*i for i in range(5)]
print(q)

print("\n##################################\n")