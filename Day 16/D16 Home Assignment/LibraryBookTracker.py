'''8.	Library Book Tracker
o	Create a class Book:
	Attributes:
	title, author, copies_available.
	Methods:
	issue() – Decrease copies if available.
	return_book() – Increase copies.
	status() – Shows book status.'''
class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available
    def issue(self):
        if self.copies_available > 0:
            self.copies_available -= 1
        else:
            print("Copies Unavailable")
    def return_book(self):
        self.copies_available += 1
    def status(self):
        print(f"Title of Book : {self.title}")
        print(f"Author : {self.author}")
        print(f"Copies Available : {self.copies_available}")

b = Book("Wings of Fire", "Dr. APJ Abdul Kalam", 15)
b.issue()
b.issue()
b.issue()
b.return_book()
b.status()
        