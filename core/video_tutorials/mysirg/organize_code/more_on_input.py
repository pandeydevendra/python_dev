x = eval(input("Enter anything: "))
print(x, type(x))
a, b, c = [int(x) for x in input("Enter three numbers: ").split()]
print(a, b)
print(c, type(c))
# eval() will work better here too...
a, b, c = [eval(x) for x in input("Enter a, b, c: ").split()]
print(a, type(a))
print(b, type(b))
print(c, type(c))

# for tuple:
t = tuple([eval(x) for x in input("Enter tuples: ").split()])
print(t, type(t))
# for set:
s = set([eval(x) for x in input("Enter set: ").split()])
print(s, type(s))

# for dict:
d = dict(input("Enter dict: ").split('-') for _ in range(3))
print(d, type(d))

d1 = {x: input("Enter Name: ") for x in range(1, 5)}
print(d1, type(d1))

d2 = {input("key"): input("value") for r in range(3)}
print(d2, type(d2))
