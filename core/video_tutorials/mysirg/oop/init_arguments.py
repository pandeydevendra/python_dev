class Test:
    def __init__(self, x, y):
        self.a = x
        self.b = y


t1 = Test(30, 40)
print(t1.a, t1.b)
t2 = Test(100, 200)
print(t2.a, t2.b)
print(type(t1))
print("")
s1 = Test("Hello!", "Hi!!")
print(s1.a, s1.b)
print(type(s1))
print("")
d1 = Test({1,2,3.5}, {2, "name", 2.5})
print(d1.a, d1.b)
print(type(d1))

