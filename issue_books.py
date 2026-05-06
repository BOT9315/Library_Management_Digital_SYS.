from utils import books, issue_books, renumber_books

def issue():
    book_name = input("Enter the book name: ").upper()
    matches = [key for key, name in books.items() if name == book_name]
    if not matches:
        
        print("This Book is not available in our library.\nSorry for the inconvenience.\nThank you for using our library.\nHave a nice day.")
    elif len(matches) == 1:
        
        target_key = matches[0]
        issue_books[target_key] = books.pop(target_key)
        renumber_books()
        print("\n|->Book assigned successfully.\n|-> You have 15 days to return this book.\n\nThank you for using our library.\nHave a nice day.\n\n***For fine details read below.***")
        print(".\n.\n.\n.\n.")
        print("## 📜 Return & Fine Policy")
        print("Users are encouraged to return books promptly. Fines are calculated automatically upon return based on the following schedule:\n")
        print("| Days Kept | Status | Fine Applied |\n| :--- | :--- | :--- |\n| **1 - 15 Days** | On Time | No Fine (₹0) |\n| **16 - 20 Days** | Overdue | ₹10 per overdue day |\n| **21 - 30 Days** | Severely Overdue | ₹20 per overdue day |\n| **31+ Days** | Defaulted | ₹50 per day + Account Suspension |")
        print("\n> **Note:** Fines are mandatory and must be cleared before the user can issue any new books.")
    else:
        print("Available copies:")
        for i, key in enumerate(matches, start=1):
            print(f"{i}. {books[key]}")
        while True:
            choice_input = input("Enter the number of the book you want to issue: ").strip()
            if not choice_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue
                
            choice = int(choice_input)
            if 1 <= choice <= len(matches):
                target_key = matches[choice-1]
                issue_books[target_key] = books.pop(target_key)
                renumber_books()
                print("\n|->Book assigned successfully.\n|-> You have 15 days to return this book.\n\nThank you for using our library.\nHave a nice day.\n\n***For fine details read below.***")
                print(".\n.\n.\n.\n.")
                print("## 📜 Return & Fine Policy")
                print("Users are encouraged to return books promptly. Fines are calculated automatically upon return based on the following schedule:\n")
                print("| Days Kept | Status | Fine Applied |\n| :--- | :--- | :--- |\n| **1 - 15 Days** | On Time | No Fine (₹0) |\n| **16 - 20 Days** | Overdue | ₹10 per overdue day |\n| **21 - 30 Days** | Severely Overdue | ₹20 per overdue day |\n| **31+ Days** | Defaulted | ₹50 per day + Account Suspension |")
                print("\n> **Note:** Fines are mandatory and must be cleared before the user can issue any new books.")
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(matches)}.")

