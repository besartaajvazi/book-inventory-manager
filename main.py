
# A list to hold the books
inventory = []
 
def add_book():
    print()
    print("Adding a New Book..")
    print()
        
    title = input("Title> ")
    author = input("Author> ")
    isbn = input("ISBN> ")
    callnumber = input("CallNumber> ")

    if title and author and isbn:

    # Add the book as a dictionary
        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "callnumber": callnumber
        }

    inventory.append(book)
    print("\nBook added successfully!\n")

def view_books():
    print("\nCurrent Books in Inventory:")
    if not inventory:
        print("No books available.")
        return

    for book in inventory:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']}")
    print()

def delete_book():
    try:
        book_id = int(input("Enter ID of the book to delete> "))
        for book in inventory:
            if book['id'] == book_id:
                inventory.remove(book)
                print("Book deleted.")
                return
        print("Book not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    print()

def search_book():
    book_id = int(input("Enter ID of the book to search: "))

    found = False
    for book in inventory:  
        if book['id'] == book_id:
            print("\nThe book exists:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            found = True
            break

    if not found:
        print("\nNo book found with that ID.")