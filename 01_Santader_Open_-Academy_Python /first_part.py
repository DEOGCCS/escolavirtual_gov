# escrever a primeira mensagem de código Hello World.
from itertools import count

print ("Hello World")
"""
Para além de "#" podemos usar três " para conseguir realizar
textos de várias linhas.
"""

# Basics
# Data Types
age = 18 #integer
height = 13.5 #float
name = "David" #string
under_age = age >= 18 #boolean
#print(under_age)

# Operators
a = 10
b = 3
"""
sum = a + b #13
print(sum)
subtraction = a - b #7
print(subtraction)
multiplication = a * b #30
print(multiplication)
division = a / b #3,33
print(division)
floor_division = a // b #3
print(floor_division)
modulus = a % b #1
print(modulus)
exponentiation = a ** b #1000
print(exponentiation)

#comparisons

equal = a == b
print(equal)
not_equal_to = a != b
print(not_equal_to)
greater_then = a > b
print(greater_then)
lesser_then = a < b
print(lesser_then)
greater_equal_then = a >= b
print(greater_equal_then)
lesser_equal_then = a <= b
print(lesser_equal_then)

# Logical
result_and = (a < 11) and (b > 2)
print(result_and)
return_or = (a < 11) and (b < 2)
print(result_and)
return_not = not (a > 5)
print(return_not)

#conditions structure
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

grade = 30

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Average")
else:
    print("Need improvement")
"""

# Loops
#for
fruits = ["apple", "banana", "orange"]
"""
for fruit in fruits:
    print(fruit)

for i in range(1, 6):
    print(i * 2)

#while
counter = 1

while counter < 6:
    print(counter)
    counter += 1

while counter <= 6:
    print(counter * 2)
    counter += 1
    if counter == 3:
        break

for i in range(10):
    if i % 2 == 0: #irá filtrar os numeros impares pois ao dividir por dois não resulta em 0
        continue #irá sltar todos os números pares
    print(i)

for i in range(5):
    pass # irá passar para a proxima linha de código sem fazer nada
# lists
print(fruits[2])

fruits.append("grapes")
print(fruits)
fruits.insert(1,"lemons")
print(fruits)
fruits.remove("lemons")
print(fruits)
remove_fruits = fruits.pop (2)
print(fruits)
print(remove_fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

number = [1,2,3,4,5]
square = [x ** 2 for x in number if x % 2 == 0]
print(square)

# Tuple
points = (1, 2, 3, 4, 2, 3, 1, 0)

print(points.count(2))
print(points.index(3))
print(points.index(3,3, 7))
print(len(points))

#Dictionaries
person = {"name":"David", "age":36, "city":"Edimburgo"}
print(person.keys())
print(person.values())
print(person.items())

update_dic = {"profession":"teacher"}
person.update(update_dic)
print(person)
"""
#sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = set1 - set2
print(difference)

sistematic_diference = set1 ^ set2
print(sistematic_diference)
