G = 6.67*10**(-11)# this is gravitational constant
def cal_g_force(m, M, r):
    f = G*m*M/(r*r)
    return f


m = int(input("mass of the 1st body in kg:"))
M = int(input("mass of the 2nd body in kg:"))
r = int(input("distance between the two body in m:"))
f = cal_g_force(m, M, r)
print("Gravitational force between the two bodies is = {0} N".format(f))