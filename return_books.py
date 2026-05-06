from utils import issue_books, books, renumber_books
#renumber _books why it is use ?

def return_book():
    book_name = input("Enter book name: ").upper()
   
    all_books = list(books.values()) + list(issue_books.values())
    if book_name in all_books:
        if book_name in issue_books.values():
            for key, value in list(issue_books.items()):
                if value == book_name:
                   issue_books.pop(key)
                   books[len(books)+1] = book_name
                   renumber_books()
                   print("Book returned.\nThank you, For using our library.\nHopefully you enjoy it.")
                   break
        else:
            print("This book is available in the library but not issued to you.\nThank you.")
    else:
        print("This book does not exist in our library.\nThank you.")
