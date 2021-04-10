"""
    5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if - else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
"""

alien_colors = ('green', 'yellow', 'red')
print(alien_colors)
print(type(alien_colors))
alien_color = "green"
if alien_color == 'green':
    print(alien_color == 'green')  # boolean output: T/F
    print("Good! You have shot a {} alien and you just earned 5 points.".format(alien_color))
if alien_color != 'green':
    print(alien_color != 'green')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 10 points.".format(alien_color))

alien_color = 'yellow'
if alien_color == 'green':
    print(alien_color == 'green')  # boolean output: T/F
    print("Good! You have shot a {} alien and you just earned 5 points.".format(alien_color))
if alien_color != 'green':
    print(alien_color != 'green')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 10 points.".format(alien_color))

print("\nAnother Version:\n")
alien_color = "green"
if alien_color == 'green':
    print(alien_color == 'green')  # boolean output: T/F
    print("Good! You have shot a {} alien and you just earned 5 points.".format(alien_color))
else:
    print(alien_color != 'green')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 10 points.".format(alien_color))
alien_color = "red"
if alien_color == 'green':
    print(alien_color == 'green')  # boolean output: T/F
    print("Good! You have shot a {} alien and you just earned 5 points.".format(alien_color))
else:
    print(alien_color != 'green')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 10 points.".format(alien_color))
