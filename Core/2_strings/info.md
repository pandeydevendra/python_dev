>>> name = "devendra pandey"
>>> name
'devendra pandey'
>>> type(name)
<class 'str'>
>>> name.title()
'Devendra Pandey'
>>> name.upper()
'DEVENDRA PANDEY'
>>> name.lower()
'devendra pandey'

user input from keyboard(CLI)

>>> x = input("hello")
hello
>>> x
''
>>> x=input("enetr name")
enetr nameDevendra
>>> x
'Devendra'
>>> n = int(input("Enter a number:"))
Enter a number:65
>>> n
65
>>> n = int(input("Enter a number:"))
Enter a number:name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'name'
>>> n=input("Enter a number:")
Enter a number:25
>>> n
'25'
>>> type(n)
<class 'str'>
>>> m=int(n)
>>> m
25
>>> type(m)
<class 'int'>
>>> m+n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> n=input("Enter a complex number:")
Enter a complex number:2+4j
>>> n
'2+4j'
>>> type(n)
<class 'str'>
>>> class(n)
  File "<stdin>", line 1
    class(n)
         ^
SyntaxError: invalid syntax
>>> 

