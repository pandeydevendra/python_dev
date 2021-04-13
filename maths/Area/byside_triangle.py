import math

def tri_side_area(a, b, c):
    p = a + b + c
    s = p/2  # half of the perimeter of triangle
    if (s<a) or (s<b)  or (s<c):
        A = "impossible to calculate by this method"
        return (p,s,A)
    else:
        A = math.sqrt(s * (s - a) * (s - b) * (s - c))  # area of triangle of any shape
        return (p,s,A)
def progress():
    a = int(input("enter side1 of the triangle:"))
    b = int(input("enter side2 of the triangle:"))
    c = int(input("enter side3 of the triangle:"))
    peri,semi_peri, area = tri_side_area(a,b,c)
#    s_area = tri_side_area(a,b,c)
    print("the triangle with sides {0}, {1}, and {2} has perimeter {3}.".format(a, b, c, peri))
    print("the triangle with sides {0}, {1}, and {2} has semi-perimeter {3}.".format(a, b, c, semi_peri))
    print("the area of the triangle with sides {0}, {1}, and {2} is {3}.".format(a, b, c, area))

keep_on = True
while(keep_on is True):
    ch = input("continue?? y/n: ")
    if ch=='y':
        progress()
    elif ch=='n':
        keep_on = False
        print("the end.")
    else:
        print('''error?????
        select valid choice''')