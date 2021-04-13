# A Dictionary of Similar Objects:
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python', }
print(favorite_languages)
"""
When you know you’ll need more than one line to define
a dictionary, press enter after the opening brace. Then indent the next
line one level (four spaces), and write the first key-value pair, followed by
a comma
Once you’ve finished defining the dictionary, add a closing brace on a
new line after the last key-value pair and indent it one level so it aligns with
the keys in the dictionary.
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
"""
This example also shows how you can break up a long print statement
over several lines. The word print is shorter than most dictionary names, so
it makes sense to include the first part of what you want to print right after
the opening parenthesis u. Choose an appropriate point at which to break
what’s being printed, and add a concatenation operator ( + ) at the end of
the first line v. Press enter and then press tab to align all subsequent lines
at one indentation level under the print statement. When you’ve finished
composing your output, you can place the closing parenthesis on the last
line of the print block w.
"""
print("\nEdwar's favorite_languages: ", favorite_languages['edward'])
print("Phil's favorite language is " +
      favorite_languages['phil'].title() +
      ".")