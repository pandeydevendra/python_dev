def cal_sum(N):
    s = N * (N + 1) / 2
    return s


N = int(input("Enter the value of N: "))
sum = int(cal_sum(N))
print("Sum of first {} natural numbers is {}".format(N, sum))

# Second Method:
"""N = int(input("Enter the value of N: "))
x1 = 1
sum_N = x1
#print(x2)

while x1 <= N:
    # print(x1)
    sum_N = x1 + 1
    print(sum_N)
    x1 = x1 + 1
# summ = num1 +"""
