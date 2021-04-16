"""
# y = 2x + 1
y = f(x)



"""
import matplotlib.pyplot as plt


def f(x):
    y_at_x = 2 * x + 1
    return y_at_x


x = [number for number in range(-10, 11)]
print(x)
y = [f(x_p) for x_p in x]
print(y)

plt.plot(x, y)
plt.xlabel("x--->")
plt.ylabel("y--->")
plt.title("2x + 1")
plt.show()
