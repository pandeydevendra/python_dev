def calculate_total (exp):
    total  = 0
    for item in exp:
        total=total+item
        return total

tom_exp_list = [100,200,500]
john_exp_list = [300,400,600]

toms_total=calculate_total(tom_exp_list)
john_total=calculate_total(john_exp_list)

print("Tom's total expences is {0}:".format(toms_total))
print("Tom's total expences is {0}:".format(john_total))

