import sys

sys.path.append('/calc_module/')
import calc_module
from calc_module.math import *

print(responses[0])
print(responses[1])
while True:
    print()  # to change line
    text = input("Enter your question/query: ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_numbers_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except Exception as e:
                print("Some Error", e)
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break

        else:
            sorry()
