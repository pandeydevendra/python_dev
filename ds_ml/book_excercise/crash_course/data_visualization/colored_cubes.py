import matplotlib.pyplot as plt

x_values = [x for x in range(1, 5001)]
print(x_values)
y_values = [x ** 3 for x in x_values]
print(y_values)


def color_scatter():
    # plt.plot(x_values, y_values, color='green', linewidth=4)
    plt.scatter(x_values, y_values, color='green', linewidth=4)
    plt.title("Cube-Plot:(y = x^3)", color='red')
    plt.xlabel("X-->>", color='blue')
    plt.ylabel("Y-->>", color='blue')
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


def colors_scatter():
    plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
    # plt.scatter(x_values, y_values, c=(0.5, 0, 0.5), edgecolor='none', s=40)
    plt.title("Cube Numbers", fontsize=10)
    plt.xlabel("X--Values-->>", fontsize=10)
    plt.ylabel("Y--Cube-Values-->>", fontsize=10)
    # Set the range for each axis:::
    # plt.axis([0, 1100, 0, 1100000])
    plt.show()


# Colormap: You might make low values a light color and high values a darker color....

def colormap_scatter():
    # plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
    # plt.scatter(x_values, y_values, c=(0.5, 0, 0.5), edgecolor='none', s=40)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)
    plt.title("Cube Numbers", fontsize=10)
    plt.xlabel("X--Values-->>", fontsize=10)
    plt.ylabel("Y--Cube-Values-->>", fontsize=10)
    # Set the range for each axis:::
    # plt.axis([0, 1100, 0, 1100000])
    plt.show()


color_scatter()
colors_scatter()
colormap_scatter()
