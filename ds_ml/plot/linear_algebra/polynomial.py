import matplotlib.pyplot as plt

x = [x_p for x_p in range(-3, 4)]
y = [(x_p) ** 2 + 2 * (x_p) - 2 for x_p in x]
print(x, "\n", y)
plt.plot(x, y)
plt.xlabel("x-->")
plt.ylabel("y-->")
plt.title("polynomial")
plt.show()
