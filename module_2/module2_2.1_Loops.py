#LOOPS 'for'
for i in range(10): # não é preciso especificar o início, 0.
    print(i) #começa com 0, mas nunca imprime o limite estabelecido.
print("\n")

# limites
for x in range(2, 10):
    print(x)
    # 1.º parametro indica posição inicial (inclusiva),
    # 2.º parametro india final (exclusiva)
print("\n")

#incrementação
for u in range(0, 10, 3):
    print(u)
    # 1.º parametro indica posição inicial (inclusiva).
    # 2.º parametro india final (exclusiva).
    # 3.º parametro está referente ao valor incremental.
print("\n")

#indexação de ‘string’
string = "hello World!"
#i = 11
#print(len(string))
#print(string[i]) #podemos indexar caso dermos o valor a indexar, se queremos masi temos de usar un 'for'
for i in range(0, len(string)):
    print(str(i) + ".º letter is " + string[i])
print("\n")

#con incremento
for x in range(0, len(string), 2):
    print(str(x) + ".º letter is " + string[x])
print("\n")

#LOOP 'While'
count = 0 #ponto de partida
while (count < 10): #limite
    print(count)
    count += 1 #incrementação

#break
while True:
    user = input("write something: ")
    if user == "end":
        print("Terminated program!")
        break
    print(user)
print("\n")

# versão sem 'break'
end = False
while end == False:
    user = input("write you name: ")
    if user == "end":
        print("end of program!")
        end = True
    else:
        print(user)
print("\n")

#Continue
    # com while
count = 1
while count + 1 <= 20:
    if count % 5 == 0:
        print("Skip")
        count += 1
        continue
    print(count)
    count += 1
print("\n")

    #com for
for i in range(0, 20):
    if i % 5 == 0:
        print("Skip")
    print(i)
