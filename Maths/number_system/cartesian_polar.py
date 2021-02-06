import math
from math import sin,cos,pi
x = float(input("Enter x: "))
y = float(input("Enter y: "))

r = (x**2+y**2)**0.5
theta = math.atan(y/x)
d = 180*theta/pi

print("r =",r," d =",d)