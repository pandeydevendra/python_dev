requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#Checking Whether a Value is in a List
"""
vins@vinay-2021:~$ python
Python 2.7.16 (default, Apr  9 2019, 04:50:39) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
>>> 
"""
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(requested_toppings)
if 'mushrooms' in requested_toppings:
    print("mushrooms is in list: \tTrue!")
else:
    print("mushrooms is in list: \tFalse")
if 'pepperoni' in requested_toppings:
    print("pepperoni is in list: \tTrue!")
else:
    print("pepperoni is in list: \tFalse!")