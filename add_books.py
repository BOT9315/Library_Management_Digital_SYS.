from utils import books, renumber_books

def add():
    book_name = input("Enter the Book name which you want to add in the library: ").upper()
    books[len(books)+1] = book_name
    renumber_books()
    print(f"Book added successfully: {book_name}")
    for idx, value in enumerate(books.values(), start=1):
        print(f"{idx}.{value}")
