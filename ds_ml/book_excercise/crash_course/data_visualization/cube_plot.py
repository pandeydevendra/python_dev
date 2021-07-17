import matplotlib.pyplot as plt

x_values = [x for x in range(1, 6)]
print(x_values)
y_values = [x ** 3 for x in x_values]
print(y_values)

plt.plot(x_values, y_values, linewidth=5)
plt.title("Cube-Plot:(y = x^3)")
plt.xlabel("X-->>")
plt.ylabel("Y-->>")
plt.tick_params(axis='both', labelsize=14)
plt.scatter(x_values, y_values, edgecolor='red', s=20)
plt.show()