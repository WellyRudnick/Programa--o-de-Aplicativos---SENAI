notas = [8.0, 5.5, 9.3, 7.6, 3.1]
print(notas[0])
print(notas[1])
print(notas[2])
print(notas[3])
print(notas[4])

print("\n\n##################################\n\n")

notas2 = [8.0, 5.5, 9.3, 7.6, 3.1]

print(notas2[0]+2)

notas2[3] = 0.5

print(notas2)

print("\n\n##################################\n\n")

notas3 = [8.0, 5.5, 9.3, 7.6, 3.1]

for i in range(5):
    print(notas3[i])

print("\n\n##################################\n\n")

notas4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    notas4[i] = 5*i

print(notas4)

print("\n\n##################################\n\n")

notas5 = [8.0, 5.5, 9.3, 7.6, 3.1]

for i in range(len(notas5)):
    print(notas5[::-1])