"""
input = comma separated numbers,
operation=
output= print even numbers, odd numbers in separate list"""

odd_num = []
even_num = []

num = input("enter numbers separated by comma: ")
num = num.split(',')
for n in num:
    n = int(n)
    if n % 2 == 0:
        even_num.append(n)
    else:
        odd_num.append(n)

print("even numbers {0}".format(even_num))
print("odd numbers {0}".format(odd_num))

"""from pylab import plot,show
y = [ 1.0, 2.4, 1.7, 0.3, 0.6, 1.8 ]
plot(y)
show()"""