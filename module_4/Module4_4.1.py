#Programação orientada a objeto
class library_book:
    pass #indica que está vazia

my_book = library_book()
print(my_book)

#Verificar o tipo de um objeto
print(type(my_book))
#ou
print(isinstance(my_book,library_book))

#init
class library(object):
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.year = pub_year
        self.call_number = call_no
        self.check_out = False

book = library("harry potter", "JK Rolling", "1998", "PZ7.R79835")
#Podemos adicionar o nome a dar na library
print(book.author)

