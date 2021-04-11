"""
#1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
"""
alien_colors = ['green', 'yellow', 'red']
print(alien_colors)
print(alien_colors[0].title())
alien_color = alien_colors[0]  # 'green'
print(alien_color)
if alien_color == 'green':
    print("Wow! You have shot a {} alien.\nYou got 5 points.".format(alien_color))
else:
    pass

alien_color = alien_colors[-1]  # 'red'
if alien_color == 'red':
    print("Wow! You have shot a {} alien.\nYou got 15 points.".format(alien_color))
if alien_color == 'green':
    print("Wow! You have shot a {} alien.\nYou got 5 points.".format(alien_color))
# version of the program, passes the if test and another fails. (The version that fails will have no output.)
alien_color = alien_colors[1]  # 'yellow'
print("\nAlien's color is '{}'.".format(alien_color))
if alien_color == 'yellow':
    print("That's great! You have shot a {} alien.\nYou just earned 10 points.".format(alien_color))
if alien_color != 'yellow':
    pass
