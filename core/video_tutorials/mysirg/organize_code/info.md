1. Input::
   
(a) eval function : (evaluate) 
x = eval(input("Enter anything: "))

'eval'  is a function which takes any type of value;
like int, float, complex, string, dict, list etc..

(b) split();
x,y = input("Enter x and y").split()

output : it's output is list of string;  i.e. ['', '']

to convert it into int... 

a, b, c = [int(x) for x in input("Enter a, b, c: ").split()]

eval() will work better here too...
a, b, c = [eval(x) for x in input("Enter a, b, c: ").split()]

for dict:
d = dict(input("Enter dict: ").split('-') for _ in range(n))
ask for range n as n = input("Enter range: ")
