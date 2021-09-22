import matplotlib.pyplot as plt

x_values = [x for x in range(1, 6)]
print(x_values)
y_values = [x ** 3 for x in x_values]
print(y_values)


def scatter_point():
    plt.scatter(1, 8)
    plt.show()


def scatter_function():
    plt.scatter(2, 8, s=200)
    # Set chart title and label axes..
    plt.title("Cube Numbers", fontsize=24)
    plt.xlabel("X-Values-->", fontsize=14)
    plt.ylabel("c of Values-->", fontsize=14)
    # Set size of tick labels..
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def scatter_square():
    # plt.scatter(x_values, y_values, s=100)
    # plt.plot(x_values, y_values, linewidth=5)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
    plt.title("Cube Numbers", fontsize=20)
    plt.xlabel("X--Values-->>", fontsize=14)
    plt.ylabel("Y--Cube-Values-->>", fontsize=14)
    plt.tick_params(axis='both', labelsize=14)  # font size of indexes(1,2,3...25)
    plt.show()


def cube_plot():
    plt.plot(x_values, y_values, linewidth=5)
    """plt.plot(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
    AttributeError: 'Line2D' object has no property 'cmap'"""
    plt.title("Cube-Plot:(y = x^3)")
    plt.xlabel("X-->>")
    plt.ylabel("Y-->>")
    plt.tick_params(axis='both', labelsize=14)
    plt.scatter(x_values, y_values, edgecolor='red', s=20)
    plt.show()


scatter_point()
scatter_function()
scatter_square()
cube_plot()
