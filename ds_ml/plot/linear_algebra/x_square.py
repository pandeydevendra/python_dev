"""
# y = 2x + 1
y = f(x)



"""
import matplotlib.pyplot as plt

x = [number for number in range(-10, 11)]
print(x)
y = [x_p ** 2 for x_p in x]
print(y)

plt.plot(x, y)
plt.xlabel("x--->")
plt.ylabel("y--->")
plt.title("x^2")
plt.show()
