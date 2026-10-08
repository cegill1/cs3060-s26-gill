class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

        def info(self):
            print(f"'{self.title}' by {self.author}")

class PDF:
    def __init__(self, file_size_mb):
        self.file_size_mb = file_size_mb

    def pdf_info(self):
        print(f"PDF file size: {self.file_size_mb} MB")

# Ebook inherits from BOTH book and PDF
class EBook(Book, PDF):
    def __init__(self, title, author, file_size_mb, format_):
        Book.__init__(self, title, author)
        PDF.__init__(self, file_size_mb)
        self.format_ = format_

    def full_info(self):
        self.info()         # from book
        self.pdf_info()     # from PDF
        print(f"Format: {self.format_}")

# Usage
ebook = EBook("1984", "George Orwell", 2, "EPUB")
ebook.full_info()