#conjunto - set
ex1 = {0,1,1,3,2,2,3,3} #estrutura de dados mutável que armazena objetos não duplicados e imutáveis e ordena os elementos em ordem ascendente.
print(ex1) # Cada elemento do conjunto é único

ex2 ={j for j in range(10)}
print(ex2)

#set.add()
ex2.add(2)
print(ex2)
ex2.add(50)
print(ex2)
print("\n")

#convert a list into a set
list1 = [0,1,2,3,4,5]
list_to_set = set(list1)
print(list_to_set)

#convert a set into a list
set1 = {j for j in range(10)}
set_to_list = list(set1)
print(set_to_list)

#concert a set into a tuple
set2 = {j for j in range(1,11,2)}
set_to_tuple = tuple(set2)
print(set_to_tuple)
print("\n")
