# sum of first N natural numbers:
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(5))
def print_sum():
    n = int(input("Enter n: "))
    s = sum(n)
    print("Sum is", s)
print_sum()


# 1. first N natural numbers:

def n_naturals(n):
    if n > 0:
        n_naturals(n - 1)
        print(n, end=" ")


n_naturals(5)

print("\n")


def rev_n_naturals(n):
    if n > 0:
        print(n, end=" ")
        rev_n_naturals(n - 1)


rev_n_naturals(5)

print("\n")
# first N even natural numbers:

def even_naturals(n):
    if n > 0:
        even_naturals(n - 1)
        print(2 * n)


even_naturals(5)


def rev_even_naturals(n):
    if n > 0:
        print(2 * n, end= " ")
        rev_even_naturals(n - 1)


rev_even_naturals(5)


print("\n")
def odd_naturals(n):
    if n > 0:
        odd_naturals(n - 1)
        print(2 * n - 1)


odd_naturals(5)


def rev_odd_naturals(n):
    if n > 0:
        print(2 * n - 1, end= " ")
        rev_odd_naturals(n - 1)


rev_odd_naturals(5)

print("\n")
def square_naturals(n):
    if n > 0:
        square_naturals(n - 1)
        print(n ** 2)


square_naturals(5)


def rev_square_naturals(n):
    if n > 0:
        print(n ** 2, end= " ")
        rev_square_naturals(n - 1)


rev_square_naturals(5)

print("\n")
def cube_naturals(n):
    if n > 0:
        cube_naturals(n - 1)
        print(n ** 3)


cube_naturals(5)


def rev_cube_naturals(n):
    if n > 0:
        print(n ** 3, end= " ")
        rev_cube_naturals(n - 1)


rev_cube_naturals(5)

# Python code to find sum
# of natural numbers upto
# n using recursion

# Returns sum of first
# n natural numbers
# def recurSum(n):
#     if n <= 1:
#         return n
#     return n + recurSum(n - 1)
#
#
# # Driver code
# n = 5
# print(recurSum(n))