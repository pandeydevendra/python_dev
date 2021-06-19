import matplotlib.pyplot as plt

def plot_square():
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares)
    plt.show()


def plot_full_sqr():
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares, linewidth=5)
    # Set chart title and label axes.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


def complete_plot():
    input_values = [1, 2, 3, 4, 5]
    squares = [x ** 2 for x in input_values]
    # print(squares)
    plt.plot(input_values, squares, linewidth=5)
    plt.title("Square Numbers", fontsize=20)
    plt.xlabel("X--Values-->>", fontsize=14)
    plt.ylabel("Y--Square-Values-->>", fontsize=14)
    plt.tick_params(axis='both', labelsize=14) # font size of indexes(1,2,3...25)
    plt.show()

plot_square()
plot_full_sqr()
complete_plot()
