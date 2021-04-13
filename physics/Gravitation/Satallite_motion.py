from math import log,exp,sin,cos,sqrt,pi,e
G = 6.67e-11 #m 3 kg − 1 s − 2 is Newton’s gravitational constant
M = 5.97e+24 #kg is the mass of the Earth, and
R = 6371e3 #m is its(Earth) radius.

def Cal_altitude(T):
    h = (M*T**2/4*pi**2)**(1/3) - R
    return h

def ask_input():
    T = float(input("Enter the time period of the satellite in s: "))
    alt_sat = Cal_altitude(T)
    print("The altitude of the satellite with T {0} s is {1} m.".format(T,alt_sat))

keep_on  = 1
while keep_on==1:
    ch = input("Do you want to continue? y/n: ")
    if ch=='y':
        ask_input()
    elif ch=='n':
        keep_on = 0
        print("End of the program")
    else:
        print("Entered choice is wrong. Please enter a correct choice. ")