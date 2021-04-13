def cal_force_a(m,u,t,v):
    a=(v-u)/t
    f = m*(v-u)/t
    return (a,f)  # it returns tuple


m = int(input("mass of the body in kg:"))
u_0 = int(input("initial velocity of the body in m/s:"))
t_f = int(input("time of motion in s:"))
v_f = int(input("final velocity of the body in m/s:"))

a,f = cal_force_a(m, u_0, t_f, v_f) # call actual function: here " cal_force_a "

print("acceleration of the body:", a)
print("force acting on the body=", f)