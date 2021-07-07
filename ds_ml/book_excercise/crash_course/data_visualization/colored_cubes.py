import matplotlib.pyplot as plt

x_values = [x for x in range(1, 5001)]
print(x_values)
y_values = [x ** 3 for x in x_values]
print(y_values)

plt.plot(x_values, y_values, color='green', linewidth=4)
plt.title("Cube-Plot:(y = x^3)", color='red')
plt.xlabel("X-->>", color='blue')
plt.ylabel("Y-->>", color='blue')
plt.tick_params(axis='both', labelsize=14)
plt.show()