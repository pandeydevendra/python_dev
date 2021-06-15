To handle 'Run Time Error' ; not Syntax Error:
1.
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("Sum is ", x + y)
No Error.....

2.
    x = int(input("Enter x: "))
    y = input("Enter y: ")
    print("Sum is ", x + y)
    
TypeError as x is int but y is not
    
3.
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("Division is ", x/y)
    
Possible Errors: TypeError, ValueError, ZeroDivisionError etc

> # Raising Exceptions:
# In Order as follow::
    try:
    except 
    except
    else
    finally
try is followed by at least one except or finally block
means except will not come without try....
except can be of any number 0,1, or more times
but finally will come only once at most or not at least. finally may or may not appear

esle runs when no exception raises....
finally runs always..




