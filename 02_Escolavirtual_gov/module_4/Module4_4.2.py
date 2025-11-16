#Metodos
class librarybook(object):
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.year = pub_year
        self.call_number = call_no

    def title_and_author(self):
        return "{} {}: {}".format(self.author[1], self.author[0], self.title)
    def __str__(self):
        return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title)
    def __repr__(self):
        return "<Book: {} ({})>".format(self.title, self.call_number)

new_book = librarybook("Harry Potter and the Sorcerer's Stone", ("Rowling","J.K."), 1998, "PZ7.R79835")

print(new_book)
print(new_book.title_and_author())
print(new_book.__repr__())

