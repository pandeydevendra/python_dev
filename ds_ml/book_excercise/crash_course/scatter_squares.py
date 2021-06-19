import matplotlib.pyplot as plt


def scatter_point():
    plt.scatter(2, 4)
    plt.show()


def scatter_function():
    plt.scatter(2, 4, s=200)
    # Set chart title and label axes..
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("X-Values-->", fontsize=14)
    plt.ylabel("Square of Values-->", fontsize=14)
    # Set size of tick labels..
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def scatter_square():
    x_values = [1, 2, 3, 4, 5]
    y_values = [x ** 2 for x in x_values]
    plt.scatter(x_values, y_values, s=100)
    # plt.plot(x_values, y_values, linewidth=5)
    plt.title("Square Numbers", fontsize=20)
    plt.xlabel("X--Values-->>", fontsize=14)
    plt.ylabel("Y--Square-Values-->>", fontsize=14)
    plt.tick_params(axis='both', labelsize=14)  # font size of indexes(1,2,3...25)
    plt.show()


def final_scatter():
    x_values = list(range(1, 1001))
    y_values = [x ** 2 for x in range(1, 1001)]
    print(y_values)
    # plt.scatter(x_values, y_values, s=20)
    plt.scatter(x_values, y_values, edgecolor='none', s=20)
    plt.title("Square Numbers", fontsize=10)
    plt.xlabel("X--Values-->>", fontsize=10)
    plt.ylabel("Y--Square-Values-->>", fontsize=10)
    # Set the range for each axis:::
    plt.axis([0, 1100, 0, 1100000])
    plt.show()


scatter_point()
scatter_square()
scatter_function()
final_scatter()