final = ''
x = "Mathematics is essential for many fields"
print()
print(x)
x_rev = x.split(" ")
print()
print(x_rev)

x_rev = [element[::-1] for element in x_rev]
print()
print(x_rev)
print()

for element in x_rev:
    print()
    print(element)
    final += element + ' '
    print()
    print(final)

print(final)
