# '*' is for tuple
def avg(*n):
    s = 0
    for x in n:
        s = s + x
    average = s / len(n)
    return average


print("Average is", avg(10, 20, 30))
