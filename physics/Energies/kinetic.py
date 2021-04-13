def cal_ke(m, v):
    ke = (1 / 2) * m * (v ** 2)
    return ke


m = float(input("enter mass of the body in kg:"))
v = float(input("enter velocity of the body in m/s:"))
k_energy = cal_ke(m, v)
print("kinetic energy of the body of mass {0} and velocity {1} is {2} joules".format(
    m,
    v,
    k_energy
))
