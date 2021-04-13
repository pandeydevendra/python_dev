#strings are to store 'text data; words, syntax, sentences etc...
text1="hello world"
text1[0:12]
print(text1)
#text2='let's learn python' #; this is a invalid(wrong) syntax:
text2="let's learn python" #
print(text2)
# Also
text2='let"s learn python'
text2="'let's learn python'"  #"'a'" to print 'a' .
text2='let/s learn python'

print(text2)
text2='"let"s learn python"'  #'"b"' to print "b".

# to change line use '''abc lmn opqrs''' (triple ''' coat) >>>>eg>>
text3='''siapokhar
mohania
kaimur'''
print(text3) # will give text3 'siapokhar\nmohania\nkaimur' on IDLE

s1='hello mr. Dev'
s2="let's work together"

s3=s1+" "+s2 #"a"+'b' continuous ab, 'a'+" "+"b" with space in between ; 'a b'.
print(s3)


s6="Total states in India is:" #str type
s7=28                          #int type

#s10=s6+s7 ; TypeError: must be str, not int

s10=s6+str(s7)    # change int(s7) into str by str(s7)

print(s10)

stat1="I love eating"
stat2=input("enter number of fruits:")
stat3="fruits everyday"
stat=stat1+' '+str(stat2)+' '+stat3
print(stat)
#string is immutable
