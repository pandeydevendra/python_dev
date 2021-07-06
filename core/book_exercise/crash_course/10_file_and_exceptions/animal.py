"""filename.txt contains animal names"""


def show_name(filename):
    """
    It'll read name from txt files:;
    @param filename:str
    @return: None
    """
    with open(filename) as file_object:
        print(file_object, type(file_object))
        for line in file_object:
            print(line)
            # print(line.rstrip())


def read_file_data(filename):
    """ Count the approximate number of words in a file."""
    try:
        show_name(filename)
    except FileNotFoundError:
        print(f"""Sorry, the file {filename} doesn't exist""")
    else:
        pass


filenames = ['cat.txt', 'dog.txt']
# import ipdb; ipdb.set_trace()
for filename in filenames:
    read_file_data(filename)
