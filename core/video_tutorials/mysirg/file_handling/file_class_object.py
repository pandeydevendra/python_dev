class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


students_list = [Student('Amit', 19), Student('Rahul', 20), Student('Mohit', 22), Student('Rana', 21)]


def saveStudents():
    import pickle
    f1 = open('file2.obj', 'wb')
    for s in students_list:
        pickle.dump(s, f1)
    f1.close()


def viewAllStudents():
    import pickle
    f2 = open('file2.obj', 'rb')

    s_list = []
    while True:
        try:
            s_list = s_list + [pickle.load(f2)]
        except EOFError:
            break
    return s_list


"""
# Run on console
saveStudents() # NameError: name 'saveStudents' is not defined...
saveAllStudents() # NameError: name 'saveAllStudents' is not defined...
"""
# TODO >> rectify errors