def f2():
    print("f2 inside second file")


def f3():
    print("f3 inside second file")


f3()
print("ame::::::", __name__)
if __name__ == '__main__':
    f2()

import second


def f1():
    print("f1 inside first")


f1()

# second.f2()
