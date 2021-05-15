from prettytable import PrettyTable
from dev_db import cursor, db

cur = cursor
mydb = db


def get_book_id(b_title):
    sql_query = "SELECT * FROM books WHERE title = '{}'".format(b_title)
    print(sql_query)
    cur.execute(sql_query)
    book = cur.fetchone()
    if book:
        book_id = book["id"]
        book_info = PrettyTable()
        book_info.field_names = ["id", "title", "price", "total", "available"]
        book_data = [book["id"], book['title'], book['price'], book['total'], book['available']]
        book_info.add_row(book_data)
        print(book_info)

    else:
        book_id = 0
    return book_id


def add_book(b_title, b_price, b_total, b_available):
    """
    this fn is use to add records in book table
    """
    print(b_title, b_price, b_total, b_available)
    insert_in_book = "INSERT INTO books(title, price, total, available) VALUES(%s,%s,%s,%s)"
    book = (b_title, b_price, b_total, b_available)
    cur.execute(insert_in_book, book)
    mydb.commit()


def update_book(b_id, updated_title, new_price, updated_total, updated_available):
    """
    this function is use to update records in book table
    """
    q_sql_update_table = "UPDATE books SET title = '{}', price = '{}', total = '{}', available = '{}'" \
                         " WHERE id = '{}'".format(
        updated_title, new_price, updated_total, updated_available, b_id
    )
    print(q_sql_update_table)
    cur.execute(q_sql_update_table)
    mydb.commit()


def delete(b_id):
    q_sql_del_table = "DELETE FROM books WHERE id = '{}'".format(b_id)
    print(q_sql_del_table)
    cur.execute(q_sql_del_table)
    mydb.commit()


def select():
    sql_query = "SELECT * FROM books"
    cur.execute(sql_query)
    books = cur.fetchall()
    print(books)
    print(type(books))
    return books


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
    add_book(book_title.title(), book_price, book_total, book_available)


def select_process():
    books_show = PrettyTable()
    books_show.field_names = ["Title", "Price", "Total", "Available"]
    books = select()
    for book in books:
        book_details = [book['title'], book['price'], book['total'], book['available']]
        books_show.add_row(book_details)
    print(books_show)


def update_process():
    current_title = input("Enter the book's current title: ")
    book_id = get_book_id(current_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(current_title))
    else:
        updated_title = input("Enter the book's updated  title: ")
        updated_price = float(input("Enter new price: "))
        updated_total = int(input("Enter new total number of copies: "))
        updated_available = int(input("Enter available number of copies: "))
        update_book(book_id, updated_title, updated_price, updated_total, updated_available)


def delete_process():
    book_title = input("Enter the book's title to be deleted: ")
    book_id = get_book_id(book_title)
    if book_id == 0:
        print("Book titled {} doesn't exist.".format(book_title))
    else:
        ch = input("Are you sure you want to delete {} book?y/n: ".format(book_title))
        if ch.lower() == 'y':
            delete(book_id)
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
