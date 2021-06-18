class Test:
    a = 10

    def __init__(self):
        self.x = 1
        Test.b = 20

    def f1(self):
        x = 100
        self.x = 2
        Test.c = 30

    def f2(m, n):
        print(n)
        Test.d = 40


t1 = Test()
t1.f2(3)
print("")
Test.f2(2, 5)
