def sum(*n):
    s = 0
    for x in n:
        s = s + x
    return s


print("Sum is ", sum(10, 20, 30, 40, 50, 60))


def player_score(playername, *score):
    print(playername, end=' ')
    s = 0
    for x in score:
        s = s + x
    return s


r1 = player_score("Rahane's total score is ", 55, 105, 155, 85, 115)
print(r1)


def player_score(playername, *score):
    print(playername, end=' ')
    s = 0
    for x in score:
        s = s + x
    print("Total Score = ", s)


player_score("Rahane's", 55, 105, 155, 85, 115)
player_score("Kohli's", 110, 20, 0, 135, 185)


def player_score(*score, playername):
    print(playername, end=' ')
    s = 0
    for x in score:
        s = s + x
    return s


r = player_score(55, 105, 155, 85, 115, playername="Rahane's Final Sum =")
print(r)

print()
"""
def player_score(*score, playername):
    print(playername, end=' ')
    s = 0
    for x in score:
        s = s + x
    print("Total Score = ", s)


player_score("Rahane's", 55, 105, 155, 85, 115) 
player_score("Kohli's", 110, 20, 0, 135, 185)
# TypeError: player_score() missing 1 required keyword-only argument: 'playername'
"""


def player_score(*score, playername):
    print(playername, end=' ')
    s = 0
    for x in score:
        s = s + x
    print("Total Score = ", s)


player_score(55, 105, 155, 85, 115, playername="Rahane's")
player_score(110, 20, 0, 135, 185, playername="Kohli's")
