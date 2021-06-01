responses = ["Welcome to my calculator", "My name is Dev_calc", "Thanks",
             "Sorry, I can't resolve your query"]


def extract_numbers_from_text(text):
    l = []
    for t in text.split(' '):
        print(t)
        try:
            l.append(float(t))
            print(l)
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


def end():
    print(responses[2])
    print("Press enter key to exit..")
    exit()


def my_name():
    print(responses[1])


def sorry():
    print(responses[-1])


operations = {"PLUS": sum, "ADD": sum, "ADDITION": sum, "SUM": sum, "MINUS": substract, "SUBSTRACT": substract,
              "SUBSTRACTION": substract, "PRODUCT": product, "MULTIPLY": product
              }

commands = {"EXIT": end, "END": end, "STOP": end, "NAME": my_name}
