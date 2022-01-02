import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(x, y):
    m = b = 0
    iterations = 100
    n = len(x)
    learning_rate = 0.06
    for i in range(iterations):
        y_predicted = m * x + b
        cost = (1 / n) * (sum([val ** 2 for val in (y - y_predicted)]))
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m = m - learning_rate * md
        b = b - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m, b, cost, i))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)
