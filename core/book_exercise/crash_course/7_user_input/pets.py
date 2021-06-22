pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"pets: {pets}")
while 'cat' in pets:
    pets.remove('cat')

print(f"pets: {pets}")

while 'dog' in pets:
    pets.remove('dog')

print(f"pets: {pets}")