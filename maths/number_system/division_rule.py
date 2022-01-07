def decor_except_handle(func):
    """

    @param func: function
    @return: function
    """

    def inner_exception(a, b):
        if b == 0:
            print("math error!!")
        else:
            func(a, b)

    return inner_exception


@decor_except_handle
def division_rule(a,b):
    d = a / b
    print(f"{a}/{b} = {d}")



# def enter_two_nums():
#     a = int(input("Enter a number a: "))
#     b = int(input("Enter a number b: "))
#     return a, b
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
# print(f"division_rule ::: {division_rule}")
# innterfn = decor_except_handle(division_rule)
# print(f"innterfn ::: {innterfn}")
# innterfn(a, b)

division_rule(a,b)
