
>>> x=True
>>> y=int(x)
>>> y
1
>>> int(False)
0
>>> bool(0)
False
>>> bool(8)
True
>>> "ABC"< "BCD"
True
>>> "vt">"uv"
True
>>> "vt"=="uv"
False
>>> 6!=9
True
>>> 1+2j==2+4j
False
>>> 1+2j>=2+4j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'complex' and 'complex'
>>> True+5
6
>>> False+8
8
>>> 5*False
0
>>> 5>4>3
True
>>> 8>5<7
True
>>> x==5>4>3
False
>>> x=5>4>3
>>> x
True
>>> int(x0
... int(x)
  File "<stdin>", line 2
    int(x)
      ^
SyntaxError: invalid syntax
>>> int(x)
1
>>> "AD">3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
>>> "AD">=3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> "AD"=3
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> "AD"==3
False
>>> 3+4j==3+4j
True
>>> 5=="5"
False
>>> 'a'==45
False
>>> a==45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> ord('a')==45
False
>>> ord('a')==97
True
>>> ord('a')==87
False
>>> ord('a')==79
False
>>> ord
<built-in function ord>
>>> ord(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> ord('a')
97
>>> ord('b')
98
>>> ord('z')
122
>>> ord('A')
65
>>> ord('Z')
90
>>> ord('AB')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 2 found
>>> ord('A'+'B')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 2 found
>>> 5==5.0
True
>>> 5=='5'
False
>>> '5'=="5"
True
>>> True==1
True
>>> True==2
False
>>> True==5
False
>>> False==0
True
>>> False==4
False
>>> True<=4
True
>>> False!=True
True
>>> 
>>> 3>4 and 5>4
False
>>> 3!=4 and 10<20
True
>>> 3>4 or 5>4
True
>>> 5 and 4
4
>>> 2 and 4
4
>>> 4 and 4
4
>>> 3 or 5
3
>>> 5 or 3
5
>>> a and b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> 'a' and 'b'
'b'
>>> 'a' or 'b'
'a'
>>> 0 or 2
2
>>> 2 or 0
2
>>> True or False
True
>>> True and False
False
>>> x=_
>>> x and True
False
>>> not x
True
>>> not 3==3
False
>>> not 0
True
>>> not 0+oj
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'oj' is not defined
>>> not 0+0j
True
>>> not""
True
>>> not "avbh"
False
>>>  "avbh" or "bvhy" 
  File "<stdin>", line 1
    "avbh" or "bvhy" 
    ^
IndentationError: unexpected indent
>>>  "avbh" and "bvhy" 
  File "<stdin>", line 1
    "avbh" and "bvhy" 
    ^
IndentationError: unexpected indent
>>> 3 and 4>3
True
>>> 2 and 3+4
7
>>> 4 and y+6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> 4 and y==6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> 3 or 5/0
3
>>> 3 nd 5/0
  File "<stdin>", line 1
    3 nd 5/0
       ^
SyntaxError: invalid syntax
>>> 3 and 5/2
2.5

'compound assignment'
>>> x=2
>>> x
2
>>> x+=4
>>> x
6
>>> y=4
>>> y-=2
>>> 
>>> y
2
>>> c=x*y
>>> c
12
>>> c/=3
>>> c
4.0
>>> c*=3
>>> c
12.0
>>> x
6
>>> x5//=3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x5' is not defined
>>> 5//=3
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> x//2
3
>>> x/2
3.0
>>> x%2
0
>>> x%%2
  File "<stdin>", line 1
    x%%2
      ^
SyntaxError: invalid syntax
>>> x^2
4
>>> x
6
>>> 6^2
4
>>> x^=2
>>> x*4
16
>>> x-
  File "<stdin>", line 1
    x-
     ^
SyntaxError: invalid syntax
>>> x-= 10
>>> x
-6
>>> x+ = 10
  File "<stdin>", line 1
    x+ = 10
       ^
SyntaxError: invalid syntax
>>> x+ = 10
  File "<stdin>", line 1
    x+ = 10
       ^
SyntaxError: invalid syntax
>>> x+= 10
>>> x
4
>>> x*=2+3
>>> x
20
>>> 
>>> 
>>> x||=5
  File "<stdin>", line 1
    x||=5
       ^
SyntaxError: invalid syntax
>>> x
20
>>> x//=5
>>> x
4
>>> x/=4
>>> x
1.0
>>> x*=3+4
>>> x
7.0
>>> 

Identity operator
>>> x=5
>>> y=5
>>> id(x)
8825664
>>> id(y)
8825664
>>> bin(x)
'0b101'
>>> bin(y)
'0b101'
>>> x is y
True
>>> x==y
True
>>> x=y
>>> y
5
>>> y=6
>>> x is y
False
>>> x==y
False
>>> bin(y)
'0b110'
>>> id(y)
8825696
>>> 
>>> x=5
>>> y=5.0
>>> x==y
True
>>> x is y
False
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> bin(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
>>> x is not y
True
>>> not x is y
True
>>> not x == y
False
>>> not x==y
False
>>> 

member operator

>>> x = "abc"
>>> a in x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> "a" in x
True
>>> "A" not in x
True
>>> "A" is  not in x
  File "<stdin>", line 1
    "A" is  not in x
                 ^
SyntaxError: invalid syntax
>>> "a" is in x
  File "<stdin>", line 1
    "a" is in x
            ^
SyntaxError: invalid syntax
>>> y = 3456
>>> 3 in y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: argument of type 'int' is not iterable
>>> y = "3456"
>>> 3 in y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'in <string>' requires string as left operand, not int
>>> x = [ 1,2,4,5,7,8,9]
>>> 5 in x
True
>>> y = 3,4,6,8,9
>>> 6 in y
True
>>> 


input / output

>>> y=2*x
>>> print(x,y)
10 20
>>> print(x,",",y)
10 , 20
>>> print(x,y, sep=",")
10,20
>>> print("Hello", end=".")
Hello.>>> print("students", end="!.")
studprint(x,",",y)
10 , 20
>>> exit()
vins@vins-Vostro-2520:~$ print(x)
bash: syntax error near unexpected token `x'
vins@vins-Vostro-2520:~$ python3
Python 3.6.8 (default, Apr  9 2019, 04:59:38) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> print("value of x is %d" %x)
value of x is 5
>>> y=15
>>> print("value of %d and %d is %d" %(x,y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not enough arguments for format string
>>> print("value of x=%d and y=%f" %(x,y))
value of x=5 and y=15.000000
>>> print("value of x=%d and y=%d" %(x,y))
value of x=5 and y=15
>>> print("value of x is %d and  =%d" %(x,y))
[1]+  Stopped                 python3
vins@vins-Vostro-2520:~$ python3
Python 3.6.8 (default, Apr  9 2019, 04:59:38) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("value of x is %d and y is %d" %(x,y))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x=4
>>> y=6
>>> print("value of x is %d and y is %d" %(x,y))
value of x is 4 and y is 6
>>> z=x+y
>>> z
10
>>> print("value of x is %d,  y is %d and z is %d" %(x,y,z))
value of x is 4,  y is 6 and z is 10
>>> z=x+y
>>> print("sum of  %d and %d is %d" %(x,y,z))
sum of  4 and 6 is 10
>>> z=x+y
>>> print("value of x is %d,  y is %d and z is %d" %(x,y,z))
value of x is 4,  y is 6 and z is 10
>>> a=5
>>> b=9
>>> c=a+b
>>> print("value of a is %d,  b is %d and c is %d" %(a,b,c))
value of a is 5,  b is 9 and c is 14
>>> print("sum of  %d and %d is %d" %(a,b,c))
sum of  5 and 9 is 14
>>> print("x=%g"
... c=a+b
  File "<stdin>", line 2
    c=a+b
    ^
SyntaxError: invalid syntax
>>> print("x=%g"%x)
x=4
>>> n=devendra
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'devendra' is not defined
>>> n="devendra"
>>> print("Hello, ",n, "x=",x, "y=",y, "a=", a)
Hello,  devendra x= 4 y= 6 a= 5
>>> 
> 
> 
operator replacement

>>> print("sum of {} and {} is {}".format(a,b,c))
sum of 5 and 9 is 14

>0 1 2 ... is by default corresponding to the order of a b c .... 
>>> print("Hello {} x is {} y is {} and z is {}".format(n,x,y,z))
Hello devendra x is 4 y is 6 and z is 10
>>> print("Hello {0} x is {1} y is {2} and z is {3}".format(n,x,y,z))
Hello devendra x is 4 y is 6 and z is 10
>>> print("Hello {0} x is {1} y is {2} and z is {3}".format(x,y,z,n))
Hello 4 x is 6 y is 10 and z is devendra
>>> gt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'gt' is not defined
>>> print("Hello {3} x is {0} y is {1} and z is {2}".format(x,y,z,n))
Hello devendra x is 4 y is 6 and z is 10
>>> 
