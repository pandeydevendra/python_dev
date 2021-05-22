'''from itertools import combinations
input = ['a', 'b', 'c', 'd']
output = sum([map(list, combinations(input, i)) for i in range(len(input) + 1)], [])


from itertools import combinations

input = ['a', 'b', 'c', 'd']
output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
'''

import itertools
a = [1, 2, 3, 4]
for i in range(0, len(a) + 1):
    print
    list(itertools.combinations(a, i))
#TODO