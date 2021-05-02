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


def add_student(name, age, fee):
    """
    this function will save student's data into table
    """
    print(name, age, fee)
    insert_in_student = "INSERT INTO students(name, age, fee) VALUES(%s,%s,%s)"
    student = (name, age, fee)
    cur.execute(insert_in_student, student)
    mydb.commit()


def add_student_process():
    """

    """
    name = input("Enter student's name: ")
    age = int(input("Enter the age of the student: "))
    fee = float(input("Enter the fee of the student: "))
    add_student(name, age, fee)


def manage_student():
    action_ch = input("Which operation do you want; CRUD: ")
    action = action_ch.upper()
    if action == 'C':
        add_student_process()
    elif action == 'R':
        fetch_student_process()
    elif action == 'U':
        print("Work in Progress")
    elif action == 'D':
        print("Work in Progress")
    else:
        print('''Wrong input!! enter valid choice: ''')


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
