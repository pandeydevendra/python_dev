places = ['siliconvalley', 'trivendram', 'paris', 'berlin', 'darban']
print(places)
print("Number of places are = ", len(places))
print(sorted(places, reverse=True))
print("\nActual list unaltered:")
print(places)

places.reverse()
print("\tOrder of the list has changed:")
print(places)

places.reverse()
print("\nOrder of the list has changed back to original:")
print(places)

places.sort()  # with no input to sort, just for alphabetical
print("\nlist has arranged in alphabetical order:")
print(places)
places.sort(reverse=True)  # with input reverse=Ture;to reverse list order
print("\tOrder of the list has changed to reversed alphabetically:")
print(places)
print("Number of places are = ", len(places))
