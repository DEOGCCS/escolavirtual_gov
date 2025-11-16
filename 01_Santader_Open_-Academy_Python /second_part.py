"""
def hello():
    print("Hello World")

hello()

#Parameters and arguments
def greetings(name):
    print(f"Hello {name}!")

greetings("David")

#Return values
def sum(a,b):
    return a+b

result = sum(3,4)
print(result)

#lambda
square = lambda x : x**2
print(square(5))

#input
name = input("What's your name: ")
age = input("How old are you: ")

print("Hello "+name+"!")
print("You are "+age+" years old.")

age2 = int(input("How old are you: "))
if age2 >= 18:
    print("You are an adult.")
else:
    print("you are under age.")

#output

print(f"hello my name is {name} and i'm {age}years old!")

x = 5
y = "3"
z = x + int(y)
print(z)
"""
#files

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

with open("data.txt", "r") as file:
    content = file.read()
print(content)
