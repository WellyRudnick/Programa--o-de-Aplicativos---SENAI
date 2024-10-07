import numpy as np

print("\nExemplo 1\n")

a = np.array([1, 2, 3])
print(a.ndim)
print(a.size)
print(a)

print("\nExemplo 2\n")

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.ndim)
print(b.size)
print(b)

print("\nExemplo 3\n")

c = np.arange(10)
print(c)
c = np.arange(10).reshape(2, 5)
print(c)

print("\nExemplo 4\n")

d = np.zeros(3, dtype=int)
print(d)
d = np.zeros((3, 4),dtype=int)
print(d)

print("\nExemplo 5\n")

e = np.ones((2, 3))
e += 1
print(e)