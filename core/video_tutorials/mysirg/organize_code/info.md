> # Formal/Default Arguments:
def sum(a,b,c)  all a,b & c ask values 
def(a, b = 0, c = 1)

After default argument all later variable should be of default value
ie. def sum(a,b=2,c=3) okk
but, def sum(a=0, b, c=1) incorrect:::; b must take a default value

> # Positional/Keyword Arguments:
position == order
keyword == direct value
def sum(a,b)
    ----------
    ----------
sum(10,20), sum(10, b=20) --> a = 10 & b = 20
sum(20,10), sum(20,b=10)  -->  a = 20 & b = 10
sum(a=10,b=20), sum (b=20,a=10) -> a = 10 & b = 20 ::;
will give same result of sum = 30 without any error.
But,
sum(10,a=10),  sum(a=10,20), sum(b=20,10) etc will give errors...

Note >> After Keyword argument all later variable should be of Keyword value (not positional argument)
i.e.
sum(positional,positional) ....ok
sum(positional, keyword) ....ok
sum(keyword, positional) .... incorrect
sum(keyword,keyword) ....ok



> # 1. Input::
   
#(a) eval function : (evaluate) 
x = eval(input("Enter anything: "))

'eval'  is a function which takes any type of value;
like int, float, complex, string, dict, list etc..

#(b) split();
x,y = input("Enter x and y").split()

output : it's output is list of string;  i.e. ['', '']

to convert it into int... 

a, b, c = [int(x) for x in input("Enter a, b, c: ").split()]

eval() will work better here too...
a, b, c = [eval(x) for x in input("Enter a, b, c: ").split()]

for dict:
d = dict(input("Enter dict: ").split('-') for _ in range(n))
ask for range n as n = input("Enter range: ")