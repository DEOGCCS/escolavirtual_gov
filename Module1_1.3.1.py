#Declarações condicionais
#Estruturas condicionais if

x=7
y=49

if (x*2 == y):
    print("y is double of x")
elif (x**2 == y):
    print("y is the square of x")
else:
    print("y is not a double of x")

"""
EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"

Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação 
para o valor inserido ou irá imprimir "invalid inputs" para todos os outros números.
"""
numb = input("insert a number")
if numb == '0':
    print("0")
elif numb == '1':
    print("1")
elif numb == '2':
    print("2")
elif numb == '3':
    print("3")
elif numb == '4':
    print("4")
elif numb == '5':
    print("5")
elif numb == '6':
    print("6")
elif numb == '7':
    print("7")
elif numb == '8':
    print("8")
elif numb == '9':
    print("9")
else:
    print("invalid inputs")
