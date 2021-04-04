"""
#method 1 simple maths:
monkey climbing_up_rate = 3 units/time
monkey sliding_down_rate = 1 unit/time
net_climbing_rate = 3 - 1 = 2 units/(time)

pole_height = 15 units

# note: "monkey slides down till it reaches top"
net_height = pole_height - climbing_up_rate = 15 - 3*'1' = 12 units (remaining height) @ 1 unit of time

time = net_height/net_climbing_rate
total time =  time + 1

"""
"""
#method 2: loop method
H_0 = pole_height = 15
climbing_up = 3
sliding_down = 1

h_cover = 0  
stop when h_cover < pole height
if h_cover < pole_height: 0 < 15
at hr_1 = 
h_cover = 3-1 = 2 m
if h_cover < pole_height: 2 < 15
at hr_2 =
h_cover = h_cover + 2  4
and so on

"""

pole_height = int(input("Enter pole height: "))
up_rate = int(input("Enter climbing speed: "))
down_rate = int(input("Enter sliding speed: "))
# net_up_rate = up_rate - down_rate
h_cover = 0
t = 0
total_upward_covered = 0
total_downward_covered = 0
h_remain = pole_height
keep_on = True
while keep_on is True:
    if t > 10:
        break
    h_cover = h_cover + up_rate
    h_remain = h_remain - up_rate
    print(h_cover)
    print(h_remain)
    # if h_remain < up_rate:
    #   up_rate = h_remain
    total_upward_covered = total_upward_covered + up_rate
    if h_cover < pole_height:
        h_cover = h_cover - down_rate
        h_remain = h_remain + down_rate
        total_downward_covered = total_downward_covered + down_rate
    else:
        keep_on = False
    t = t + 1
print("time = {} hrs.".format(t))
print("Total upward covered height is {}.".format(total_upward_covered))
print("Total downward covered height is {}.".format(total_downward_covered))
