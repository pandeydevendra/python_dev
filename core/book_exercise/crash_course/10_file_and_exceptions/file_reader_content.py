with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

    print(contents.rstrip())

message = "I really like dog."
print(message)
message.replace('dog', 'cat')
print(message)