alien_0 = {'color': 'green', 'points': 5}
print("alien_dictionary: {}".format(alien_0))
print(alien_0['color'])
print("Marks:", alien_0['points'])
"""
dictionaries: In Python, a dictionary is wrapped in braces, {} ,
 with a series of key-value pairs inside the brace
"""
new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!")
# Adding New Key-Value Pairs:
print(alien_0, "\n")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# Starting with an Empty Dictionary:
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 15
print("\nnew_alien_dict:", alien_0)
# Modifying Values in a Dictionary:
alien_0 = {'color': 'green'}
print("\nThe alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # This must be a fast alien.
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# speed : slow;
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
print("speed is ", alien_0['speed'])
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # This must be a fast alien.
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
print("\nOriginal x-position: " + str(alien_0['x_position']))
print("speed is ", alien_0['speed'])
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # This must be a fast alien.
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

print("\n")
# Removing Key-Value Pairs:Be aware that the deleted key-value pair is removed permanently.
alien_1st = {'color': 'green', 'points': 5}
print(alien_1st)
del alien_1st['points']
print(alien_1st)
