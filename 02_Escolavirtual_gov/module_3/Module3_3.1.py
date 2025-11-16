#list - Listas
list1 = ["David", "36", "Casado"]
print("Você se chama " + list1[0] +".")

#list.insert(local na lista, informação a adicionar)
list1.insert(1,"Gomes")
print("O seu nome de familia é " + list1[1] + ".")

#list.append(adiciona informação no final da lista)
list1.append("programador")
print("A sua profissão é " +list1[4]+".")

#list.remove(remove o elemento desejado)
print(list1)
list1.remove("programador")
print(list1)

#list.pop(posição no index)
list1.pop(3)
print(list1)

#list.sort()
list1.sort()
print(list1)

#len - temos de tornar o número e uma string
print("esta lista tem " + str(len(list1)) +" itens.")

#",".join(list)
"/".join(list1)
print(list1)

#list of list
index1 = []
index1.append([1,2,3])
index1.append(["a", "b", "c"])
print(index1)
print(index1[1])
print(index1[1][2])
