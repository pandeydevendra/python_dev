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
    h_cover = h_cover + up_rate
    h_remain = h_remain - up_rate
    #print("h_cover:", h_cover)
    #print("h_remain: ", h_remain)
    #print("total_upward_covered: ", total_upward_covered)

    if h_remain < up_rate:
        h_remain = h_remain if h_remain > 0 else 0
        #print("h_remain is < up_rate: ", h_remain)
        total_upward_covered = total_upward_covered + h_remain
    else:
        total_upward_covered = total_upward_covered + up_rate

    if h_cover < pole_height:
        #print("h_cover < pole_height :: ", h_cover, pole_height)
        h_cover = h_cover + up_rate
        h_remain = h_remain + down_rate
        total_downward_covered = total_downward_covered + down_rate
    else:
        keep_on = False
    t = t + 1

print("time = {} hrs.".format(t))
print("Total upward covered height is {}.".format(total_upward_covered))
print("Total downward covered height is {}.".format(total_downward_covered))
# distance and displacement
# total_upward_covered,  total_upward_covered => distance
# h_cover =>displacement
