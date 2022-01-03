import pickle


class Calculation:
    def add_num(self, a, b):
        print(a + b)


cal_obj = Calculation()

FILENAME = "add_2_nums.pkl"


def save_addition_model():
    with open(FILENAME, 'wb') as f_obj:
        pickle.dump(cal_obj, f_obj)


save_addition_model()

with open(FILENAME, 'rb') as f:
    obj = pickle.load(f)

obj.add_num(4, 6)
