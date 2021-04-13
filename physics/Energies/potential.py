g = 9.81
def cal_pe(m,h):
    pe=m*g*h
    return pe


m = float(input("enter mass of the body in kg:"))
h = float(input("enter the height of the body from the reference point in m:"))
p_energy = cal_pe(m,h)
print("potential energy of mass {0} and height {1} is {2} joules".format(
    m,
    h,
    p_energy
))