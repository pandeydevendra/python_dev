# parrot = input("Tell me to repeat something: ")
# print(parrot)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# print(message)
# print(prompt)
# while message != 'quit':
#     message = input(prompt)
#     print(message)
# if message != 'quit':
#     print(message)

# Loop using: FLAG ::: True/False...

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)