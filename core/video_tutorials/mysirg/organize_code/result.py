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