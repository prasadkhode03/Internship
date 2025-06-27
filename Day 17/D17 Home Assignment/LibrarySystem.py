'''25.	Library System:
o	Create parent class LibraryItem.
o	Create child classes:
	Book: title, author.
	Magazine: title, issue_number.
	DVD: title, duration.
o	Implement a method display() for each.'''
class LibraryItem:
    def __init__(self, title):
        self.title = title
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    def display(self):
        print("\nBook Title : ", self.title)
        print("Book Author : ", self.author)
class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number
    def display(self):
        print("\nMagazine Title :", self.title)
        print("Issue Number :", self.issue_number)
class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
    def display(self):
        print("\nDVD Title : ", self.title)
        print("DVD Duration : ", self.duration)
book = Book("Wings of Fire", "APJ Abdul Kalam")
magazine = Magazine("Captain America", "54316")
dvd = DVD("Taarein Zamin Par", "02.40hrs")
book.display()
magazine.display()
dvd.display()