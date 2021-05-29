import database as lms_db


def add_student_process():
    """

    """
    name = input("Enter student's name: ")
    age = int(input("Enter the age of the student: "))
    fee = float(input("Enter the fee of the student: "))
    lms_db.add_student(name, age, fee)


def update_student_process():
    current_name = input("Enter the student's current name: ")
    student_id = lms_db.get_student_id(current_name)
    if student_id == 0:
        print("Student named {} doesn't exist.".format(current_name))
    else:
        updated_name = input("Enter the student's updated name: ")
        updated_age = float(input("Enter current age: "))
        updated_fee = int(input("Enter new fee: "))
        lms_db.update_student(student_id, updated_name, updated_age, updated_fee)


def delete_student_process():
    student_name = input("Enter the student's name to be deleted: ")
    student_id = lms_db.get_student_id(student_name)
    if student_id == 0:
        print("Student named {} doesn't exist.".format(student_id))
    else:
        ch = input("Are you sure you want to delete {} student?y/n: ".format(student_name))
        if ch.lower() == 'y':
            lms_db.delete_process(student_id)
        else:
            print("Thank you! Student's record is safe in our lms.")


def manage_student():
    action_ch = input("Which operation do you want; CRUD: ")
    action = action_ch.upper()
    if action == 'C':
        add_student_process()
    elif action == 'R':
        lms_db.fetch_student_process()
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


if __name__ == "__main__":
    start_program()
