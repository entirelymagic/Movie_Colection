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
    """The menu of the application"""
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


def find_book():
    """
        Find a book by author or name of the book.
        Currently must provide the exact notations.
    """
    
    def look_after_name_or_author(expected, finder):
        found = []
        books = database.get_all_books()
        
        for book in books:
            if finder(book) == expected:
                found.append(book)

        return found

    find_by = input("What property are you seraching by? name or author: ")
    looking_for = input("what are you looking for? ")
    books = look_after_name_or_author(looking_for, lambda book: book[find_by])
    return print_book_list(books)


def prompt_add_book():
    """
        Get the name and the other of the book by input and add it to the database
    """
    name = input('Enter the new book name: ')
    author = input("Enter the new book author: ")

    database.add_book(name, author)

def print_book_list(books):
    """
        A function that get a book list object and print it each book
    """
    try:
        print("""\n     Your list if books: """)
        for book in books:
            read = 'Yes' if book['read'] else 'No'
            
            print(f"{book['name']} by {book['author']}, read: {read}")
    except TypeError:
        print('Your list of books is empty!')

        
def list_books():
    """
        List the books from the database using the print_book_list function.
    """
    books = database.get_all_books()

    
    print_book_list(books)


def prompt_read_book():
    """
        Get from an input the name of the book you would like to set as read and
        modify the database.    
    """
    name = input('Enter the name of the book you finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    """
        Take the name of the book as input and delete it from the database. 
    """
    name = input("Enter then name of the book you would like to delete: ")
    check_again = input(
        f"Are you sure you would like to delete {name} book? \n \
        Type yes if you really want to delete the book: ")
    if check_again == 'yes':
        database.delete_book(name)
    else:
        print("The book was not deleted.")

if __name__ == "__main__":
    menu()
