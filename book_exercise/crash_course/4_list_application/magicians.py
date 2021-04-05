magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

for magician in magicians:
    print("\n" + magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".")

print("\nThank you everyone. That was a great magic show!")

# never miss a colon (:) at last of loop condition:
"""m
agicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)
"""

# Avoid Indentation Errors; ensure syntax for inside the loop (with indentation) or/and outside the loop (w/o indent)

# Logical Errors: program is right to Python but not getting desired output.....
"""

"""
for magician in magicians:
    print("\n" + magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".")

"""In the above 3 line program expected output are as previous ones. But since the last line is not 
indented accordingly it results in wrong output. Although the program is run by python without any error"""

# One more example of logical error:

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")
