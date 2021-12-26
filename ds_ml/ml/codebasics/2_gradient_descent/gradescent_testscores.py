import numpy as np
import pandas as pd

df = pd.read_csv("test_scores.csv")


# print(df)

# print(df.math, type(df.math))
# print(y, type(y))


def gradient_descent(x, y):
    m = b = 0
    iterations = 150
    n = len(x)
    learning_rate = -0.01
    for i in range(iterations):
        y_p = m * x + b
        cost = (1 / n) * (sum([val ** 2 for val in (y - y_p)]))
        md = -(2 / n) * sum(x * (y - y_p))
        bd = -(2 / n) * sum(y - y_p)
        m = m - learning_rate * md
        b = b - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m, b, cost, i))


y = np.array(df.math)
x = np.array(df.cs)

gradient_descent(x, y)
