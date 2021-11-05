import json

# load the data into a list......

population_file = 'population_data.json'
with open(population_file) as pf:
    population_data = json.load(pf)

    # print(population_data)

# print the population for each country for the year 2010...

for p_dict in population_data:
    if p_dict['Year'] == '2010':
        country_name = p_dict['Country Name']
        # population = p_dict['Value']  # population value in str type..
        # print(country_name + ":" + population)

# Converting Strings into Numerical Values....
        population = int(p_dict['Value'])
        # print(country_name + ":" + population) # we can't add str(country_name) with int(population) directly.
        # convert int into str ; ...str(int).. str(population). #OR  print(country_name, ":", population)

        print(country_name + ":" + str(population))
        # now; ValueError: invalid literal for int() with base 10: '1127437398.85751'


