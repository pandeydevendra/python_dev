name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age, "\nAge Type: ", type(age))
# print(age >= 50) TypeError: '>=' not supported between instances of 'str' and 'int

age = eval(age)
print(age, "\nAge Type: ", type(age))
print(age >= 50)