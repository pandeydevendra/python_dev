from prettytable import PrettyTable
from dev_db import cursor, db

cur = cursor
mydb = db


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
    cur.execute(sql_query)
    student = cur.fetchone()
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
    cur.execute(insert_in_student)
    mydb.commit()
    last_id = cur.lastrowid
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
    cur.execute(q_sql_update_table)
    mydb.commit()


def delete_process(s_id):
    del_query = "DELETE FROM students WHERE id = '{}'".format(s_id)
    print(del_query)
    cur.execute(del_query)
    mydb.commit()


def add_student_process():
    """

    """
    name = input("Enter student's name: ")
    age = int(input("Enter the age of the student: "))
    fee = float(input("Enter the fee of the student: "))
    add_student(name, age, fee)


def update_student_process():
    current_name = input("Enter the student's current name: ")
    student_id = get_student_id(current_name)
    if student_id == 0:
        print("Student named {} doesn't exist.".format(current_name))
    else:
        updated_name = input("Enter the student's updated name: ")
        updated_age = float(input("Enter current age: "))
        updated_fee = int(input("Enter new fee: "))
        update_student(student_id, updated_name, updated_age, updated_fee)


def delete_student_process():
    student_name = input("Enter the student's name to be deleted: ")
    student_id = get_student_id(student_name)
    if student_id == 0:
        print("Student named {} doesn't exist.".format(student_id))
    else:
        ch = input("Are you sure you want to delete {} student?y/n: ".format(student_name))
        if ch.lower() == 'y':
            delete_process(student_id)
        else:
            print("Thank you! Student's record is safe in our lms.")


def manage_student():
    action_ch = input("Which operation do you want; CRUD: ")
    action = action_ch.upper()
    if action == 'C':
        add_student_process()
    elif action == 'R':
        fetch_student_process()
    elif action == 'U':
        update_student_process()
    elif action == 'D':
        delete_student_process()
    else:
        print('''Wrong input!! enter valid choice: ''')


def start_program():
    keep_on = True
    while keep_on is True:
        ch_input = input("Do you want to continue? y/n: ")
        ch = ch_input.lower()
        if ch == 'y':
            manage_student()
        elif ch == 'n':
            keep_on = False
            print("program end")
        else:
            print('''Wrong input!! enter valid choice: ''')


if __name__ == "__name__":
    start_program()