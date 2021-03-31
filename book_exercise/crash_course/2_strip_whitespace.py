#Whitespacs::::
longest_word = "Pneumonoultramicroscopicsilicovolcanocon"
print(longest_word)
print("\t" + longest_word)
print("\n" + longest_word)
print("The longest  word in the english is:" + "\n\t" + longest_word)
l1 = "Python"
l2 = "Javascript"
l3 = "C"
l4 = "C++"
print("Python")
print("\tPython")
print(l1)
print("Languages:\n\tPython\n\tJavascript\n\tC\n\tC++")
state_1 = "Languages:\n\tPython\n\tJavascript\n\tC\n\tC++"
print(state_1)
print("Programming Languages:" + "\n\t" + l1 + "\n\t" + l2)
state_2 = "Languages:" "\n\t" + l1 + "\n\t" + l2 + "\n\t" + l3 + "\n\t" + l4
print(state_2)

#Stripping:::::::: to remove whitespaces within inverted comma;;;;;;;

favorite_programing_language = "  'Python' " #deliberately whitespaces have been given both sides
print(favorite_programing_language)
print(favorite_programing_language.rstrip())
print(favorite_programing_language.lstrip())
print(favorite_programing_language.strip())

#also:
favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

