"""
This file is to calculate velocity, displacement etc w.r.t 1st law of motion.
"""
def cal_v_s(u, t, a):
    v = u + a * t
    s = u * t + (1 / 2) * a * (t * t)
    return (v, s)  # it returns tuple in order i.e. 1st 'v' (bcz 1st eqn) and then 2nd 's'(2nd eqn)


u_0 = int(input("initial velocity of the body in m/s:"))
t_f = int(input("time of motion in s:"))
a_c = int(input("acceleration of the body in m/s-sqaure:"))
v_f, s = cal_v_s(u_0, t_f, a_c)
print("instantaneous velocity at time {0} =".format(t_f), v_f)
print("displacement of the body in {0} s =".format(t_f), s)
