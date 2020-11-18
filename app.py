from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'f' to find a book
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your Choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'f':
            find_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again")
        user_input = input(USER_CHOICE)


def find_book(finder):
    books = database.get_all_books()
    for book in books:
        print(finder(book))

    find_by = input("What property are you seraching by? name or author: ")
    looking_for = input(("what are you looking for? "))
    find_book(lambda book: book[find_by])


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input("Enter the new book author: ")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()

    print("""\n     Your list if books: """)
    try:
        for book in books:
            read = 'Yes' if book['read'] else 'No'
            print(f"{book['name']} by {book['author']}, read: {read}")
    except TypeError:
        print('Your list of books is empty!')


def prompt_read_book():
    name = input('Enter the name of the book you finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter then name of the book you would like to delete: ")

    database.delete_book(name)

if __name__ == "__main__":
    menu()
