def cal_reaction(force):
    reaction = -(force)
    return reaction

#if __name__ == "__main__":
f =int(input("enter force acting on a body in N:"))
r = cal_reaction(f)
print("force is {0}N, reaction is {1}N".format(f,r))