'''Create a Book Class
Attributes:
title, author, year.
Method:
get_description() — Returns a formatted description like:
"The book 'Title' by Author was published in Year."
Test it: Create a book and print its description.'''

class Book:
    def get_description(self, title, author, year):
        print(f"The book \"{title}\" by {author} was published in {year}.")

B1 = Book()
B1.get_description("Wings of Fire", "Dr. APJ Abdul Kalam", 1999)