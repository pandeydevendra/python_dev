import pickle


class Calculation:
    def add_num(self, a, b):
        print(a + b)


FILENAME = "add_2_nums.pkl"

with open(FILENAME, 'rb') as f:
    obj = pickle.load(f)

obj.add_num(4, 6)

# TODO
