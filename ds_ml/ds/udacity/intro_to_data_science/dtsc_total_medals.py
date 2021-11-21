import numpy as np
from pandas import DataFrame, Series

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                     'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                     'Austria', 'France', 'Poland', 'China', 'Korea',
                     'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                     'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                     'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

avg_gold = np.mean(gold)
print(f"Normal average of gold medals = {avg_gold}")
print(f"Normal average of silver medals = {np.mean(silver)}")
print(f"Normal average of bronze medals = {np.mean(bronze)}")

# other ways:;

golds = {'gold' : Series(gold)}
gold_df = DataFrame(golds)
gold_avg = gold_df.apply(np.mean)
print(f"{gold_avg}")

# or simply:
silver_avg = DataFrame({'silver': Series(silver)}).apply(np.mean)
print(f"{silver_avg}")

# one liner:

print(f"{DataFrame({'bronze' : Series(bronze)}).apply(np.mean)}")

# total_medals:; use 'numpy.sum()':
print(f"Total Medals: \nGolds = {np.sum(gold)} \nSilver = {np.sum(silver)} \nBronze = {np.sum(bronze)}")

# total_medals country-wise:

print(f"Total participating countries = {len(countries)}")

total_medals = np.add(gold,silver)
print(total_medals)
'''
total_medals = np.add(gold,silver,bronze)
print(total_medals) # TypeError: return arrays must be of ArrayType
'''
total_medals = np.array(gold) + np.array(silver) + np.array(bronze)
print(f"Total medals: \n{total_medals}")

def total_medals_dataframe():
    total_medals_df = DataFrame(
        {'country_name': countries,
         'gold': gold,
         'silver': silver,
         'bronze': bronze,
         'total_medal': total_medals}
    )

    return total_medals_df

print(total_medals_dataframe())