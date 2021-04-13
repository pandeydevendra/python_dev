c1 = input("enter a name:")
c2 =  ""
# for c in c1:
#     c2 = c+c2
#     print(c2)
l = len(c1)
print("length of c1 is:",l)
for i in range(l):
   #print(l - i)
    j = l -1-i
    #print(j)
    c2 = c2+c1[j]
   #print(c2)

print("reversed string is:",c2)
