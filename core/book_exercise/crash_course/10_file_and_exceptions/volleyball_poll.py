from datetime import datetime

filename = 'volleyball_rating.txt'


def get_current_date():
    today_date = datetime.today()
    date_today_str = today_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_today_str


def save_player_name_and_rating(player_name, rating):
    """

    @param player_name: str
    @param rating: int
    @return: None
    """
    current_time = get_current_date()
    with open(filename, 'a') as fp:
        fp.write(f"{current_time}: {player_name} - {rating}\n")


def ask_player_and_rating():
    user_player_name = input("Enter your name: ")
    user_game_rating = int(input("How much you rate this game (1 to 10): "))
    print(f"{user_player_name} - {user_game_rating}")
    save_player_name_and_rating(user_player_name, user_game_rating)


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?(y/n): ")
    if ch.lower() == 'y':
        ask_player_and_rating()
    elif ch.lower() == 'n':
        print("Exit.")
        keep_on = False
    else:
        print("Wrong input")
