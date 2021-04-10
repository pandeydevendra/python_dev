"""
abcd_suffle = 'aabbbccddd'
#a1a2b1b2c1c2d1d2d3==a2b2c2d3
for alphabet in abcd_suffle:
   pass
"""
s = "aabbacccdccc"
lilist_char = []
list_char.append(s[0])
#print(list_char)
s2 = ""
for i in range(1, len(s)):
   char = s[i]
   if s[i] in list_char:
      list_char.append(char)
   else:
      length = len(list_char)
      last_ele = list_char[-1]
      s2 = "{}{}{}".format(s2, last_ele, length)
      list_char = []
      list_char.append(char)

print(s2)