#Tuple
x = (1,2,3)

print(x*2)
print(x + (4,5,6))

#indexdos elementos na tupla
print(x.index(2))

#abreviação
(a,b,c) = (1,2,3)
print(c)

#converter tupla em lista
y = ("a", "b", "c", "d")
list(y)
print(y)
print(list(y))

#converte um index em tuple
c = ["ana", "bela", "ama", "nda"]
tuple(c)
print(c)
print(tuple(c))

#Associação de elementos em tuplas
person = ("David", "Gomes", 36)
first, last, age = person
print(age)

