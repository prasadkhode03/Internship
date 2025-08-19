'''Create a Book Class
Attributes:
title, author, year.
Method:
get_description() — Returns a formatted description like:
"The book 'Title' by Author was published in Year."
Test it: Create a book and print its description'''

class Book:
    title = "Ek Kahani"
    author = "Prasad Khode"
    year = 2002

    def get_description(self):
        print(f"The Book {self.title} by {self.author} was published in {self.year}")

Bk = Book()
Bk.get_description()