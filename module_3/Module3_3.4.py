#dictionary
dict = {} # uma estrutura de dados que armazena pares de valores chave nos quais as chaves DEVEM ser objetos imutáveis.

dict1 = {'a':1, 'b':10, 'c':100}
print(dict1['b'])

#actualização de valores de uma chave
dict1['b'] = 50
print(dict1['b'])

dict2 = {'greetings': 'hello world!', 'alphabet': ['a', 'b', 'c', 'd'], 'check-in': False, 'phone number': 123456789}
print(dict2['greetings'])
print(dict2['alphabet'])
print(dict2['check-in'])
print(dict2['phone number'])

dict2['alphabet'] = ['words']
print(dict2['alphabet'])
print('\n')

#find keys
print(dict2.keys())

#find values
print(dict2.values())

#items
print(dict2.items())
