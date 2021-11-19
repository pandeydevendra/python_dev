import numpy as np
from pandas import DataFrame, Series

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
# a, b ; 1-D arrays
print(np.dot(a, b))

# transpose of a matrix
print(np.transpose(a))

x = [1, 2]  # 1-D array ; a matrix., 1*2 == R*C
y = [[2, 4, 6], [3, 5, 7]]  # 2-D array ; a matrix., 2*3
print(np.dot(x, y))  # output > [1*2]*[2*3] = [1*3]

z = [[8], [9], [10]]  # 3-D array ; a matrix., 3*1 == R*C
print(np.dot(y, z))  # output > [2*3]*[3*1] = [2*1]

"""
points = {'gold' = 4, 'silver' = 2, 'bronze' = 1} 
"""
countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


def total_medal_points():
    # olympic_medal_counts = {'country_name': Series(countries), 'gold': Series(gold), 'silver': Series(silver),
    #                         'bronze': Series(bronze)}
    #
    # olympic_medal_counts_df = DataFrame(olympic_medal_counts)
    # print(olympic_medal_counts_df)

    # simple method for total_medal_points:

    medal_points = np.array(np.dot(4, gold)) + np.array(np.dot(2, silver)) + np.array(np.dot(1, bronze))
    # print(medal_points)

    olympic_point_counts_df = DataFrame(
        {
            'country': Series(countries),
            'total_points': Series(medal_points)
        }
    )
    return olympic_point_counts_df


# total_medal_points()
print(total_medal_points())

# def total_medal_points():
# point = [[[4, 2, 1]]]
# medals = [[gold], [silver], [bronze]]
# print(f"{point} \n{medals}")
# print(f"{type(point)} \n{type(medals)}")
#
# medal_points = np.dot(point,medals)
# print(f"Gold points = {medal_points}")


print(np.transpose(b))
print(f"z = {z}")
t_z = np.transpose(z)
print(f"Tanspose of z = {t_z}")
print((f"{type(t_z)}"))

print(np.dot(z, t_z))

point = [4, 2, 1]
t_point = np.transpose(point)
print(f"{point} {type(point)} \n{t_point} {type(t_point)}")

points = [[4, 2, 1]]
t_points = np.transpose(points)
print(f"{points} {type(points)} \n{t_points} {type(t_points)}")
# medals = [np.array(gold), np.array(silver), np.array(bronze)]
# medals = [[gold], [silver], [bronze]]
medals1 = [gold, silver, bronze]
# print(medals, type(np.array(medals)))
print(medals1, type(np.array(medals1)))

# total_point = np.dot(t_points, medals)
# print(f"{total_point}")

total_point = np.dot(point, medals1)
print(f"{total_point}")


# dataframe

def country_medal_total_points():
    total_medal_point_df = DataFrame(
        {
            'country': Series(countries),
            'gold': Series(gold),
            'silver': Series(silver),
            'bronze': Series(bronze),
            'total_points': Series(total_point)
        }
    )

    return total_medal_point_df


print(f"{country_medal_total_points()}")
