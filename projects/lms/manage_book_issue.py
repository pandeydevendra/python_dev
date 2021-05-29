from datetime import datetime, timedelta
from random import randint

import database as lms_db

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
    lms_db.book_assign_save_in_db(student_id, book_id, ISSUE_BOOK_STATUS, issue_date_str)


def process_book_issue():
    book_title = input("Enter the book title: ")
    book_id, book_info = lms_db.get_book_id(book_title)
    # if book_id > 0 and book_info['available'] > 0:
    if book_id < 1:
        print("The book {} does not exist.".format(book_title))
        return False
    if book_info['available'] < 1:
        print("No copy available for the {} book.".format(book_title))
        return False
    student_name = input("Enter student name: ")
    student_id = lms_db.get_student_id(student_name)
    if student_id < 1:
        print("The student named {} does not exist.".format(student_name))
        return False
    assign_book_to_student(book_id, student_id)


def get_return_date():
    days_before = randint(30, 50)
    return_date = datetime.today() - timedelta(days=days_before)
    date_return_str = return_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_return_str


def process_book_return():
    student_name = input("Enter student name: ")
    s_id = lms_db.get_student_id(student_name)
    if s_id != 0:
        print("Student id is ", s_id)
    else:
        print("{} does not exist in the student list.".format(student_name))
        proceed_loop()

    book_id_list = lms_db.get_assign_book_id_by_student(s_id)
    print(book_id_list)
    book_title = input("Enter the book title: ")
    book_id, book_info = lms_db.get_book_id(book_title)
    if book_id < 1:
        print("The book {} does not exist.".format(book_title))
        return False
    if book_id not in book_id_list:
        print("This book is not assigned to the above student")
        return False
    print("Now I have s_id {} and book_id {} ".format(s_id, book_id))
    # now we have book_id, s_id
    date_return_str = get_return_date()
    lms_db.book_return_save_in_db(RETURN_BOOK_STATUS, date_return_str, book_id, s_id)


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
