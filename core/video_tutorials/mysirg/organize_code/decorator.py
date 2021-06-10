# decorate result function:
"""
create a new function to be known as decorator funtion
"""


def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print("Congrats!! You have got distinction.")

        else:
            result_function(marks)

    return distinction


@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")


marks = [eval(x) for x in input("Enter marks: ").split(' ')]
print("Marks are: ", marks)
print(type(marks))
r = result(marks)
print(r)
