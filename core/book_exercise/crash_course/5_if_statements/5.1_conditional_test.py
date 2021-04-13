car = 'subaru'
print(car)
print(car == 'subaru')

print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\ncar != subaru: >>> False")
print(car != 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("car != audi: >>> True")
print(car != 'audi')
"""
Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False .
"""
biggest_cities = ['newyork', 'beijing', 'mumbai', 'tokyo', 'london']
print(biggest_cities)
print("\nIs mumbai in biggest_cities? I predict True.")
print('mumbai' in biggest_cities)
print("\nmumbai is not in biggest_cities. I predict False.")
print('mumbai' not in biggest_cities)
print("\nIs delhi' in biggest_cities? I predict False.")
print('delhi' in biggest_cities)
print("\ndelhi' is not in biggest_cities. I predict True.")
print('delhi' not in biggest_cities)
print("\nIs 'newyork' in biggest_cities? I predict True.")
print('newyork' in biggest_cities)
print("\nnewyork is not in biggest_cities. I predict False.")
print('newyork' not in biggest_cities)
print("\nIs tokyo in biggest_cities? I predict True.")
print('tokyo' in biggest_cities)
print("\ntokyo is not in biggest_cities. I predict False.")
print('tokyo' not in biggest_cities)
print("\nIs london in biggest_cities? I predict True.")
print('london' in biggest_cities)
print("\nlondon is not in biggest_cities. I predict False.")
print('london' not in biggest_cities)

print("\n")
count_1_10 = [number for number in range(1, 11)]
print(count_1_10)
num_1 = count_1_10[0]
print("first number in the list count_1_10 is {}.:".format(num_1), num_1 == 1)
num_10 = count_1_10[-1]
print("last number in the list count_1_10 is {}.: ".format(num_10), num_10 == 10)
print(num_1 == 0)
print(num_10 == 11)
