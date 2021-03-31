Think of your favorite m, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as 

transportation_modes = [ "Honda motorcycle", "bicycle", "car", "train", "helicopter", "hovercraft", "aircraft" ]
print(transportaion_modes)

message_1 = "“I would like to own a "
message_2 = "“I would like to pilot a "
message_3 = "“I would like to fly a "

print(message_1 + transportaion_modes[0].title() + ".")
print(message_1 + transportaion_modes[-2].title() + ".")
print(message_2 + transportaion_modes[3].title() + ".")
print(message_1 + transportaion_modes[-1].title() + ".")
print(message_3 + transportaion_modes[4].title() + ".")
print(message_1 + transportaion_modes[-5].title() + ".")
