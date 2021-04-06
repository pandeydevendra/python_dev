# Working with Part of a List:
# Slicing a List:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3], "\n")  # 1st three
print(players[1:4])  # middle three
print("\n", players[2:5])  # last three
print("last three players: \n", players[2:])  # last three
print("\n", players[-4:-1])  # middle three
print("\n", players[-3:])  # last three


# Looping Through a Slice:

print("\nHere are the first three players of my team:")
for player in players[:3]:
    print(player.title())

print("\nHere are the last three players of my team:")
for player in players[-4]:
    print(player.title())  # logical error: loop operateed on 4th from last; i.e. 'martina'

print("\nHere are the last three players of my team:")
for player in players[-3:]:
    print(player.title())

print("\nSpecial list: ")
print(players[:])  # All;  just [:], no index;;; actually a copy of original list