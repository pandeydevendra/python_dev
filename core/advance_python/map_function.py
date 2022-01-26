def circle_area(r):
    """

    @param l: int
    @param b: int
    @return: area of circle
    """

    area = 3.14 * r * r
    return area


r = int(input("Enter radius r: "))

a = circle_area(r)
print(f"area of circle with radius {r} is {a}")

# now map function:
'''
If we have a list of radius
'''

r_list = [0, 1, 2, 3, 4, 5, 6]
# list can be taken from user as well
'''
map function takes two arguments; 1>operator and 2>variable;

map(area, radius),
map(add, value)
'''

area_list = list(map(circle_area, r_list))

print(area_list)
