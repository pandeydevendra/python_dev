import matplotlib.pyplot as plt
from random_walk import RandomWalk
import ipdb

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    print(point_numbers)
    plt.plot(rw.x_values, rw.y_values, c='g')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# 
