import matplotlib.pyplot as plt


def p(x):
    f = x ** 3 - x + 2
    return f


x = []
for number in range(-5, 6):
    x.append(number)
print("x_points:     {}".format(x))
y = []
for value in x:
    y.append(p(value))
print("y_values: {}".format(y))
