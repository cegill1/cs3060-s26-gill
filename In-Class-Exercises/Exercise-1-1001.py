import types

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return  f"{self.title} checked out."
        return f"{self.title} is already checked out."

def extendReturnDate(self):
    # Update return date for the book
    return f"Return date extended 10 days"

book1 = Book("1984", "George Orwell")
book2 = Book("Wuthering Heights", "Emily Bronte")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

book2.publication_date = 1847
book2.extendReturnDate = types.MethodType(extendReturnDate, book2)