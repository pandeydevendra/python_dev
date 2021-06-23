prompt = "Please enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

print(prompt)

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to", city.title(), "!")

"""
While True requires Break......to end the program 
"""