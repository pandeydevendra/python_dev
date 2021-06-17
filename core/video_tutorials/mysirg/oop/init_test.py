class Test:
    i = 10

    def __init__(self):
        print("Hello! This is init function.")

    def f1():
        print("Hello! This is another function.")


t1 = Test()
print(t1, "\n", type(t1))

print("")
# t2 = Test()
# print(t2)
# print(t1)
print(Test.i)
print("")
Test.f1()
