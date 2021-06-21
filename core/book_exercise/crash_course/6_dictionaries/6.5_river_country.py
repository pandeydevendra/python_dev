river_country = {'Ganges': 'India', 'Nile': 'Egypt', 'Thames': 'England'}
print("The great rivers are:")
for river in river_country:
    print(river)
# print("The countries are:")
# for country in river_country:
#     print(country)
print("The great rivers are:")
for river in river_country.keys():
    print(river)
print("The countries are:")
for country in river_country.values():
    print(country)
# The Nile runs through Egypt.
print("The river : country items are:")
for item in river_country.items():
    print(item)

print(river_country.keys())
print(river_country.values())
# print("First Pair: ", r, c)
print(river_country.items())

print("New lines:")
for value in river_country:
    print(river_country[value], ":", value)
print("\nFinal result:")
for value in river_country:
    print(f"The {value} runs through {river_country[value]}.")