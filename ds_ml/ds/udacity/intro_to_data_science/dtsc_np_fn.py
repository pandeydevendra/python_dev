# numpy has multiple function like mean, median, standard deviation..,
import numpy

numbers = [num for num in range(1,11)]
print(f"Given array is {numbers}")

mean = numpy.mean(numbers)
median = numpy.median(numbers)
std = numpy.std(numbers)
print(f"Mean of the given array = {mean}")
print(f"Median of the given array = {median}")
print(f"Standard Deviation of the given array = {std}")


from pandas import DataFrame,   Series

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name' : Series(countries), 'gold' : Series(gold), 'silver' : Series(silver), 'bronze' : Series(bronze)}

olympic_medal_counts_df = DataFrame(olympic_medal_counts)
print(olympic_medal_counts_df)