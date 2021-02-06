#y=mod(x)
def get_mod(x):
    if x<0:
        y=-x
    else:
        y=x
    return y

x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[]

for px in x:
    py=get_mod(px)
    y.append(py)

print(x)
print(y)