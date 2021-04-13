"""
Alien Colors #3: Turn your if - else chain from Exercise 5-4 into an if - elif -
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
"""
alien_color = input("Enter alien color: ")
if alien_color == 'green':
    print("alien_color is {};".format(alien_color), alien_color  == 'green')  # boolean output: T/F
    print("Good! You have shot a {} alien and you just earned 5 points.".format(alien_color))
elif alien_color == 'yellow':
    print("alien_color is {};".format(alien_color), alien_color == 'yellow')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 10 points.".format(alien_color))
elif alien_color == 'red':
    print("alien_color is {};".format(alien_color), alien_color == 'red')  # boolean: T/F
    print("Great! You have shot a {} alien and you just earned 15 points.".format(alien_color))
else:
    print("Enter correct color: 'green', 'yellow', or 'red'")

# three versions ;;;;

alien_color = input("Enter alien color: ")
if alien_color == 'green':
    #print("alien_color is {};".format(alien_color), alien_color  == 'green')  # boolean output: T/F
    exclamation = "Good!"
    alien_color = 'green'
    earned_point = 5
elif alien_color == 'yellow':
    #print("alien_color is {};".format(alien_color), alien_color == 'yellow')  # boolean: T/F
    exclamation = "Great!"
    alien_color = 'yellow'
    earned_point = 10
elif alien_color == 'red':
    print("alien_color is {};".format(alien_color), alien_color == 'red')  # boolean: T/F
    exclamation = "Great!"
    alien_color = 'red'
    earned_point = 15
else:
    print("Enter correct color: 'green', 'yellow', or 'red'")

print(exclamation + " You have shot a " + alien_color +  " alien and you just earned "+ str(earned_point) + " points.")