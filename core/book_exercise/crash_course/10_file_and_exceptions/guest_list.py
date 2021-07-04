from datetime import datetime

filename = 'guest.txt'


def get_current_date():
    today_date = datetime.today()
    date_today_str = today_date.strftime("%Y-%m-%d %H:%M:%S")
    return date_today_str


def save_guest_name_in_file(guest_name):
    """

    @param guest_name: str
    @return: None
    """
    current_time = get_current_date()
    with open(filename, 'a') as fp:
        fp.write(f"{current_time} - {guest_name}\n")
        # fp.write(current_time)
        # fp.write(guest_name)
        # fp.write("\n")


keep_on = True
while keep_on is True:
    ch = input("continue? y/n: ")
    if ch == 'y':
        guest_name = input("Enter guest name: ")
        save_guest_name_in_file(guest_name)
    elif ch == 'n':
        keep_on = False
        print("the end")
    else:
        print('''error!!!enter valid choice: ''')
