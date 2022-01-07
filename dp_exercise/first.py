import second


def f1():
    print("f1 inside first")


f1()

second.f2()
s = "aabbacccdccc"
s = "aabbaaacccddccc"
list_char = []
list_char.append(s[0])
# print(list_char)
s2 = ""
for i in range(1, len(s)):
    print(s[i])
    char = s[i]

    if s[i] in list_char:
        list_char.append(char)
        print(list_char)
#     else:
#         length = len(list_char)
#         last_ele = list_char[-1]
#         s2 = "{}{}{}".format(s2, last_ele, length)
#         list_char = []
#         list_char.append(char)
#
# print(s2)
    else:
        length = len(list_char)
        last_ele = list_char[-1]
        s2 = "{}{}{}".format(s2, last_ele, length)
        list_char = []
        list_char.append(char)

print(s2)