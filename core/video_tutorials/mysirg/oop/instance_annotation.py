class Test:
    a = 10  # Static variable

    def __init__(self):
        self.x = 1  # Instance variable
        Test.b = 20  # static variable

    def f1():  # Instance Member Function
        Test.c = 30  # static variable
        # self.x = 2  # Instance variable
        # x = 100  # Local Varible

    @staticmethod
    def f2(m, n):  # Instance Method
        print(m)
        print(n)
        print(m, n)
        Test.d = 40  # static variable

    @classmethod
    def f3(cls):
        cls.e = 50
        Test.f = 60


Test.f3()
Test.g = 70

t1 = Test()
# t1.f1(3)
t1.f2(3, 4)
Test.f2(3, 4)

print(Test.__dict__)