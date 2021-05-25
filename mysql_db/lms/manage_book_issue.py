from manage_books import get_book_id
from manage_students import get_student_id
from datetime import datetime, timedelta
from random import randint
from prettytable import PrettyTable

from dev_db import cursor, db

ISSUE_BOOK_STATUS = 1
RETURN_BOOK_STATUS = 2


def get_issue_date():
    days_before = randint(50, 70)
    issue_date = datetime.today() - timedelta(days=days_before)
    date_today_str = issue_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_today_str


def assign_book_to_student(book_id, student_id):
    issue_date_str = get_issue_date()
    print(student_id, book_id)
    issue_book_query = "INSERT INTO book_issue_details SET student_id= '{}', book_id = '{}', " \
                       "issue_status = {}, issue_date = '{}'".format(
        student_id, book_id, ISSUE_BOOK_STATUS, issue_date_str
    )
    cursor.execute(issue_book_query)
    db.commit()
    last_id = cursor.lastrowid
    print(last_id)

    update_book_available = "UPDATE books SET available = available - 1 WHERE id = '{}'".format(book_id)
    cursor.execute(update_book_available)
    db.commit()


def process_book_issue():
    book_title = input("Enter the book title: ")
    book_id, book_info = get_book_id(book_title)
    # if book_id > 0 and book_info['available'] > 0:
    if book_id < 1:
        print("The book {} does not exist.".format(book_title))
        return False
    if book_info['available'] < 1:
        print("No copy available for the {} book.".format(book_title))
        return False
    student_name = input("Enter student name: ")
    student_id = get_student_id(student_name)
    if student_id < 1:
        print("The student named {} does not exist.".format(student_name))
        return False
    assign_book_to_student(book_id, student_id)


def get_assign_book_id_by_student(s_id):
    qry_get_assign_book = """SELECT student_id, book_id, issue_date, title
        FROM book_issue_details
        INNER JOIN books
        ON books.id = book_issue_details.book_id
        WHERE student_id = {} AND issue_status = 1""".format(s_id)
    print(qry_get_assign_book)
    cursor.execute(qry_get_assign_book)
    db.commit()
    list_issue = cursor.fetchall()
    print(list_issue)
    list_book_student = PrettyTable()
    list_book_student.field_names = ["Book Title", "Issue Date"]
    book_ids = []
    for book_issue in list_issue:
        print(book_issue['title'], book_issue['issue_date'])
        list_book_student_data = [book_issue['title'], book_issue['issue_date']]
        list_book_student.add_row(list_book_student_data)
        book_ids.append(book_issue['book_id'])
    print(list_book_student)
    return book_ids


def get_return_date():
    days_before = randint(30, 50)
    return_date = datetime.today() - timedelta(days=days_before)
    date_return_str = return_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_return_str


def process_book_return():
    student_name = input("Enter student name: ")
    s_id = get_student_id(student_name)
    if s_id != 0:
        print("Student id is ", s_id)
    else:
        print("{} does not exist in the student list.".format(student_name))
        proceed_loop()

    book_id_list = get_assign_book_id_by_student(s_id)
    print(book_id_list)
    book_title = input("Enter the book title: ")
    book_id, book_info = get_book_id(book_title)
    if book_id < 1:
        print("The book {} does not exist.".format(book_title))
        return False
    if book_id not in book_id_list:
        print("This book is not assigned to the above student")
        return False
    print("Now I have s_id {} and book_id {} ".format(s_id, book_id))
    # now we have book_id, s_id
    date_return_str = get_return_date()
    q_update_issue_details = "UPDATE book_issue_details " \
                             "SET issue_status = {}, return_date = '{}' " \
                             "WHERE book_id = '{}'  AND student_id = '{}'".format(
        RETURN_BOOK_STATUS, date_return_str, book_id, s_id
    )
    print(q_update_issue_details)
    cursor.execute(q_update_issue_details)
    db.commit()
    q_update_books = "UPDATE books SET available = available + 1 WHERE id = '{}'".format(book_id)
    cursor.execute(q_update_books)
    db.commit()


def manage_issue_book():
    option = input("Press i for issue a book or r for return a book: ")
    option = option.lower()
    if option == 'i':
        process_book_issue()
    elif option == 'r':
        process_book_return()
    else:
        print('''Wrong input!! enter valid choice: ''')


def proceed_loop():
    keep_on = True
    while keep_on is True:
        ch_input = input("Do you want to continue? y/n: ")
        ch = ch_input.lower()
        if ch == 'y':
            manage_issue_book()
        elif ch == 'n':
            keep_on = False
            print("program end")
        else:
            print('''Wrong input!! enter valid choice: ''')


proceed_loop()
