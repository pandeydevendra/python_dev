import pizza

pizza.pizza_making(24, 'pepperoni')
pizza.pizza_making(36, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp

mp(26, 'pepperoni')
mp(42, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')