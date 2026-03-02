import json
import os

FILE_NAME = "library_data.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def load_books():
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_books(books):
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)


def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    # Check if book ID already exists
    for book in books:
        if book["id"] == book_id:
            print(" Book ID already exists!")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    save_books(books)
    print("Book Added Successfully!")


def view_books():
    books = load_books()

    if not books:
        print("No books available.")
        return

    print("\n===== BOOK LIST =====")
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print("---------------------------------")
        print(f"ID     : {book['id']}")
        print(f"Title  : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Status : {status}")
    print("---------------------------------")


def search_book():
    books = load_books()
    search = input("Enter title to search: ").lower()

    found = False
    for book in books:
        if search in book["title"].lower():
            print(f"\nFound: {book['title']} by {book['author']}")
            found = True

    if not found:
        print(" Book not found.")


def issue_book():
    books = load_books()
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                save_books(books)
                print(" Book Issued Successfully!")
                return
            else:
                print(" Book already issued!")
                return

    print(" Book not found!")


def return_book():
    books = load_books()
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                save_books(books)
                print(" Book Returned Successfully!")
                return
            else:
                print(" Book was not issued!")
                return

    print(" Book not found!")


def delete_book():
    books = load_books()
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print(" Book Deleted Successfully!")
            return

    print(" Book not found!")


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print(" Thank you for using Library Management System!")
            break
        else:
            print(" Invalid choice! Please try again.")


if __name__ == "__main__":
    main()