import json

FILENAME = "books.json"

# Read
def read_books():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            return data["Books"]
    except FileNotFoundError:
        return []

# save
def save_books(books):
    with open(FILENAME, "w") as f:
        json.dump({"Books": books}, f, indent=4)

# display
def display_books():
    books = read_books()
    if not books:
        print("\nNo books found!\n")
    else:
        print("\n Book List:")
        for i, book in enumerate(books):
            print(f"{i}. Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")
    print()

# add
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    books = read_books()
    books.append({"Title": title, "Author": author, "Genre": genre})
    save_books(books)
    print(f"\n Book '{title}' added!\n")

# update
def update_book():
    books = read_books()
    display_books()
    try:
        index = int(input("Enter the index of the book to update: "))
        if 0 <= index < len(books):
            print("Leave blank to keep existing value.")
            title = input(f"New title ({books[index]['Title']}): ") or books[index]['Title']
            author = input(f"New author ({books[index]['Author']}): ") or books[index]['Author']
            genre = input(f"New genre ({books[index]['Genre']}): ") or books[index]['Genre']

            books[index] = {"Title": title, "Author": author, "Genre": genre}
            save_books(books)
            print(f"\n Book at index {index} updated!\n")
        else:
            print("\n Invalid index!\n")
    except ValueError:
        print("\n Please enter a valid number!\n")

# Delete
def delete_book():
    books = read_books()
    display_books()
    try:
        index = int(input("Enter the index of the book to delete: "))
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"\n Book '{removed['Title']}' deleted!\n")
        else:
            print("\n Invalid index!\n")
    except ValueError:
        print("\n Please enter a valid number!\n")

# main function
def main():
    while True:
        print("JSON Books")
        print("1. View all books")
        print("2. Add a book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
