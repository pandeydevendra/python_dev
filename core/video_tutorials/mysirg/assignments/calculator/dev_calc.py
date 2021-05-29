import sys

sys.path.append('/calc_module/')
import calc_module
from calc_module.math import *

print(responces[0])
print(responces[1])
while True:
    print()
    text = input("Enter your question/query: ")
    for word in text.split(' '):
        if word.upper() in operations.key():
            try:
                l = extract_numbers_from_text
                r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print("Some Error")
            finally:
                break
        #elif word.upper() in commands.keys()
        else:
            sorry()

# TODO // calculator implementation