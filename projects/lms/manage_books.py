from prettytable import PrettyTable

import database as lms_db


def add_book_process():
    """
    this function use to add book details such as;
    title,  price, total copies, and available copies

    initially; available_copies = total_copies as this is for new entry

    """
    book_title = input("Enter title of the book: ")
    book_price = float(input("Enter the book's price: "))
    book_total = int(input("Enter total copies of the book: "))
    book_available = book_total
    lms_db.add_book(book_title.title(), book_price, book_total, book_available)


def select_process():
    books_show = PrettyTable()
    books_show.field_names = ["Title", "Price", "Total", "Available"]
    books = lms_db.select_book()
    for book in books:
        book_details = [book['title'], book['price'], book['total'], book['available']]
        books_show.add_row(book_details)
    print(books_show)


def update_process():
    current_title = input("Enter the book's current title: ")
    book_id, _ = lms_db.get_book_id(current_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(current_title))
    else:
        updated_title = input("Enter the book's updated  title: ")
        updated_price = float(input("Enter new price: "))
        updated_total = int(input("Enter new total number of copies: "))
        updated_available = int(input("Enter available number of copies: "))
        lms_db.update_book(book_id, updated_title, updated_price, updated_total, updated_available)


def delete_process():
    book_title = input("Enter the book's title to be deleted: ")
    book_id, _ = lms_db.get_book_id(book_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(book_title))
    else:
        ch = input("Are you sure you want to delete {} book?y/n: ".format(book_title))
        if ch.lower() == 'y':
            lms_db.delete_book(book_id)
        else:
            print("Thank you! Your book is safe in our record.")


def manage_book():
    action_ch = input("Which operation do you want; CRUD: ")
    action = action_ch.upper()
    if action == 'C':
        add_book_process()
    elif action == 'R':
        select_process()
    elif action == 'U':
        update_process()
    elif action == 'D':
        delete_process()
    else:
        print('''Wrong input!! enter valid choice: ''')


def start_program():
    keep_on = True
    while keep_on is True:
        ch_input = input("Do you want to continue? y/n: ")
        ch = ch_input.lower()
        if ch == 'y':
            manage_book()
        elif ch == 'n':
            keep_on = False
            print("program end")
        else:
            print('''Wrong input!! enter valid choice: ''')


if __name__ == "__main__":
    start_program()
