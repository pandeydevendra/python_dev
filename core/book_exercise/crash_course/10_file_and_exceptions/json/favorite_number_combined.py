import json


# filename = 'favorite_number.json'

def get_stored_number():
    """Get stored number if available."""
    try:
        filename = 'favorite_number.json'
        with open(filename) as f_obj:
            f_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return f_number


def get_new_favorite_number():
    """Prompt for a new favorite_number."""
    f_number = int(input("What is your favorite_number? "))
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(f_number, f_obj)
    return f_number


def greet_user():
    """Greet the user by name."""
    f_number = get_stored_number()
    if f_number:
        print(f"""I know your favorite number! It’s {str(f_number)}.""")
    else:
        f_number = get_new_favorite_number()
        print(f"""I know your favorite number! It’s {str(f_number)}.""")


greet_user()
