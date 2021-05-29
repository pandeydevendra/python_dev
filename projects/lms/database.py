import MySQLdb
from prettytable import PrettyTable

# Open database connection
db = MySQLdb.connect("localhost", "root", "root@123", "dev_db")

# prepare a cursor object using cursor() method
# cursor = db.cursor()  # it will give tuple
cursor = db.cursor(MySQLdb.cursors.DictCursor)  # it will give dict..


# manage_books:

def get_book_id(b_title):
    """
    input: str
    return: tuple (int, dict)
    """
    sql_query = "SELECT * FROM books WHERE title = '{}'".format(b_title)
    print(sql_query)
    cursor.execute(sql_query)
    book = cursor.fetchone()
    if book:
        book_id = book["id"]
        book_info = PrettyTable()
        book_info.field_names = ["id", "title", "price", "total", "available"]
        book_data = [book["id"], book['title'], book['price'], book['total'], book['available']]
        book_info.add_row(book_data)
        print(book_info)

    else:
        book_id = 0
    return book_id, book


def add_book(b_title, b_price, b_total, b_available):
    """
    this fn is use to add records in book table
    """
    print(b_title, b_price, b_total, b_available)
    insert_in_book = "INSERT INTO books(title, price, total, available) VALUES(%s,%s,%s,%s)"
    book = (b_title, b_price, b_total, b_available)
    cursor.execute(insert_in_book, book)
    db.commit()


def update_book(b_id, updated_title, new_price, updated_total, updated_available):
    """
    this function is use to update records in book table
    """
    q_sql_update_table = "UPDATE books SET title = '{}', price = '{}', total = '{}', available = '{}'" \
                         " WHERE id = '{}'".format(
        updated_title, new_price, updated_total, updated_available, b_id
    )
    print(q_sql_update_table)
    cursor.execute(q_sql_update_table)
    db.commit()


def delete_book(b_id):
    q_sql_del_table = "DELETE FROM books WHERE id = '{}'".format(b_id)
    print(q_sql_del_table)
    cursor.execute(q_sql_del_table)
    db.commit()


def select_book():
    sql_query = "SELECT * FROM books"
    cursor.execute(sql_query)
    books = cursor.fetchall()
    print(books)
    print(type(books))
    return books


# manage_students:


def fetch_student_process():
    """
{'id': 1, 'name': 'rohan', 'age': 20, 'fee': 2000.0}
student
    """
    q1 = "SELECT * FROM students"
    print(q1)
    cursor.execute(q1)
    students = cursor.fetchall()
    # print(students)
    # print(type(students))
    show_student = PrettyTable()
    show_student.field_names = ["Id", "Name", "Age", "Fee"]
    for student in students:
        student_data = [student["id"], student["name"], student["age"], student["fee"]]
        show_student.add_row(student_data)
    print(show_student)


def get_student_id(s_name):
    sql_query = "SELECT * FROM students WHERE name = '{}'".format(s_name)
    print(sql_query)
    cursor.execute(sql_query)
    student = cursor.fetchone()
    if student:
        student_id = student["id"]
        student_info = PrettyTable()
        student_info.field_names = ["id", "name", "age", "fee"]
        student_data = [student["id"], student['name'], student['age'], student['fee']]
        student_info.add_row(student_data)
        print(student_info)

    else:
        student_id = 0
    return student_id


def add_student(name, age, fee):
    """
    this function will save student's data into table
    """
    print(name, age, fee)
    # insert_in_student = "INSERT INTO students(name, age, fee) VALUES(%s,%s,%s)"
    #  student = (name, age, fee)
    insert_in_student = "INSERT INTO students SET name= '{}', age = '{}', fee = '{}'".format(
        name, age, fee
    )
    cursor.execute(insert_in_student)
    db.commit()
    last_id = cursor.lastrowid
    last_student = PrettyTable()
    last_student.field_names = ["Id", "Name", "Age", "Fee"]
    last_student.add_row([last_id, name, age, fee])
    print(last_student)


def update_student(s_id, name, age, fee):
    """
    this function is use to update records in book table
    """
    q_sql_update_table = "UPDATE students SET name = '{}', age = '{}', fee = '{}'" \
                         " WHERE id = '{}'".format(
        name, age, fee, s_id
    )
    print(q_sql_update_table)
    cursor.execute(q_sql_update_table)
    db.commit()


def delete_process(s_id):
    del_query = "DELETE FROM students WHERE id = '{}'".format(s_id)
    print(del_query)
    cursor.execute(del_query)
    db.commit()


def book_assign_save_in_db(student_id, book_id, issue_book_status, issue_date_str):
    issue_book_query = "INSERT INTO book_issue_details SET student_id= '{}', book_id = '{}', " \
                       "issue_status = {}, issue_date = '{}'".format(
        student_id, book_id, issue_book_status, issue_date_str
    )
    cursor.execute(issue_book_query)
    db.commit()
    last_id = cursor.lastrowid
    print(last_id)

    update_book_available = "UPDATE books SET available = available - 1 WHERE id = '{}'".format(book_id)
    cursor.execute(update_book_available)
    db.commit()


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


def book_return_save_in_db(return_book_status, date_return_str, book_id, s_id):
    q_update_issue_details = "UPDATE book_issue_details " \
                             "SET issue_status = {}, return_date = '{}' " \
                             "WHERE book_id = '{}'  AND student_id = '{}'".format(
        return_book_status, date_return_str, book_id, s_id
    )
    print(q_update_issue_details)
    cursor.execute(q_update_issue_details)
    db.commit()
    q_update_books = "UPDATE books SET available = available + 1 WHERE id = '{}'".format(book_id)
    cursor.execute(q_update_books)
    db.commit()