"""The problem is as follows. A ball is dropped from a tower of height h. It has initial velocity zero and
accelerates downwards under gravity. The challenge is to write a program that asks the user to enter the height
 in meters of the tower and a time interval t in seconds, then prints on the screen the height of the ball above
 the ground at time t after it is dropped, ignoring air resistance."""
import math
g = 9.81  # gravitational acceleration

def cal_g_motion(h, t):
    h_covered = (1 / 2) * g * (t ** 2)
    if h_covered >= h:
        t_at_ground = math.sqrt(2 * h / g)
        t_at_ground = round(t_at_ground, 2)
        print("the ball has reached the ground already at {0} s.".format(t_at_ground))
        return (h, 0)
    else:
        h_reamining = h - h_covered
        return (h_covered, h_reamining)

def ask_input():
    h = float(input("enter the height of the tower in m: "))
    t = float(input("enter the time in s: "))
    h_c, h_r = cal_g_motion(h, t)
    print("total height is {0}, covered height is {1} and remaining height is {2}.".format(h, h_c, h_r))

keep_on = 1
while (keep_on == 1):
    ch = input("do you want to continue? y/n: ")
    if ch == 'y':
        ask_input()
    elif ch == 'n':
        keep_on = 0
        print("end of the program")
    else:
        print("wrong input!! Enter correct choice: ")
