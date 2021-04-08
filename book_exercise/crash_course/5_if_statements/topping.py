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
"""Testing Multiple Conditions
The if - elif - else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
However, sometimes it’s important to check all of the conditions of
interest. In this case, you should use a series of simple if statements with no
elif or else blocks. This technique makes sense when more than one condi-
tion could be True , and you want to act on every condition that is True .
Let’s reconsider the pizzeria example. If someone requests a two-topping
pizza, you’ll need to be sure to include both toppings on their pizza:"""