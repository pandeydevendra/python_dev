responces = ["Welcome to my calculator", "My name is Dev_calc", "Thanks",
             "Sorry I can't resolve your query"]


def extract_numbers_from_text(text):
    l = []
    for term in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
        return l


def sum(a, b):
    return a + b


def substract(a, b):
    return a - b


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def myname():
    print(responces[1])


def sorry():
    print(responces[-1])


def end():
    print(responces[2])
    print("Press enter key to exit..")


operations = {"PLUS": sum, "ADD": sum, "ADDITION": sum, "SUM": sum,
    "MINUS": substract, "SUBSTRACT": substract, "SUBSTRACTION": substract, "PRODUCT": product,
    "MULTIPLY": product}
