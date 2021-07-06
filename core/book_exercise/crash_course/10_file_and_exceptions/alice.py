filename = 'alice.txt'


def read_file():
    with open(filename) as f_obj:
        contents = f_obj.read()


def read_file_exception_handling():
    try:
        read_file()
    except FileNotFoundError:
        print(f"""Sorry, the file {filename} doesn't exist""")


# read_file() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
read_file_exception_handling()
print(f"""{filename}""")
