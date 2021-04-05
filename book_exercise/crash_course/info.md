	
	>>Function:
		>>>Method:
			Cases: lower(), upper() and title()
		>>>Whitespace:
			"\t" , "\n" and "\n\t"
		>>>Strip:
			rstrip(), lstrip() and strip()
		>>>append()
		>>>insert(index, value)
	>>Variable:
	>>String:
	>> Numbers:
		Integers, Floats and Complex
   
interconvertibles:
		string>> str = str(any number) = str(integer,float or complex)
		Integer>> int = int(string) = int(any words, letters)
>1. VARIABLES: Naming and Using Variables-
	•Variables can contain only letters(a-z), numbers(0-9), and underscores(_)
	•Can start with a letter or an underscore, but not with a number;viz: message_1 but not 1_message.
	•Spaces( ) are not allowed in variable names, but underscores(_) can be used to separate words in variable names. For example, greeting_message works, but greeting message will cause errors.
	•Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular programmatic purpose, such as the word print . (See “Python Keywordsand Built-in Functions” on page 489.)
	•Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better than length_of_persons_name.
	.Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

Note:
	The Python variables you’re using at this point should be lowercase. You won’t get errors if you use uppercase letters, but it’s a good idea to avoid using them for now.
@Avoiding Name Errors When Using Variables:
					Every programmer makes mistakes, and most make mistakes every day. Although good programmers might create errors, they also know how to respond to those errors efficiently.

>2. STRINGS: 
	A string is simply a series of characters. Anything(numbers, alphabets, words etc) inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:
"This is a string."
'This is also a string.'
	This flexibility allows you to use quotes and apostrophes within your strings:
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community"

>>3. List:
	Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an ele-
ment in a list, write the name of the list followed by the index of the item
enclosed in square brackets.
	In Python, square brackets ( [] ) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles:
Index Positions Start at 0, Not 1
for accessing the last element in a list. By asking for the item at index -1 ,
Python always returns the last item in the list:

>>Adding Elements to a List; "Appending" Elements to the End of a List:
'''The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list. Using the same list we had in the previous example, we’ll add the
new element 'ducati' to the end of the list:'''
>>The append() method adds 'ducati' to the end of the list without affecting any of the other elements in the list:
>> insert  :use index for desired location

>>Removing an Item Using the del Statement
'''If you know the position of the item you want to remove from a list, you can use the del statement.'''
'''You can remove an item from any position in a list using the del statement if you know its index. For example, here’s how to remove the second item, 'yamaha' , in the list:'''
'''In both examples, you can no longer access the value that was removed from the list after the del statement is used.'''

>>Removing an Item Using the pop() Method;          >pop is reciprocal to append (both works for end element by default):

'Sometimes you’ll want to use the value of an item after you remove.The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list. Let’s pop a motorcycle from the list of motorcycles:'''
>''How might this pop() method be useful? Imagine that the motorcyclesin the list are stored in chronological order according to when we owned them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought:'''
Removing an Item by Value:
''won’t know the position of the value only know the value of the item you want to remove, you can use the remove() method. For example, let’s say we want to remove the value 'ducati' from the list of motorcycles.'''
>You can also use the remove() method to work with a value that’s being removed from a list. Let’s remove the value 'ducati' and print a reason for removing it from the list:'''
The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed. You’ll learn how to do this in Chapter 7.'''

>>Making Numerical Lists: using range(initial value, one less to final value) function



>>To open terminal directly: ctrl - alt -T
>>To leave the Python prompt and return to a terminal prompt: ctrl -D or enter exit()
>>To change working directory(folder): cd ....(folder name)
>>To know about present directory: pwd
>>To see all list in the present directory: ls

Summary_chapter_01: 

	"In this chapter I learned a bit about Python in general, and I installed Python to my system. I installed a text editor to make it easier to write Python code. I learned to run snippets(small part) of Python code in a terminal session, and I ran my first actual program,hello_world.py. I probably learned a bit about troubleshooting as well.
	In the next chapter I’ll learn about the different kinds of data I can work with in my Python programs, and I’ll learn to use variables as well."

Summary_chapter_02:
	"In this chapter you learned to work with variables. You learned to use descriptive variable names and how to resolve name errors and syn- tax errors when they arise. You learned what strings are and how to display strings using lowercase, uppercase, and titlecase. You started using whitespace to organize output neatly, and you learned to strip unneeded whitespace from different parts of a string. You started working
with integers and floats, and you read about some unexpected behavior to watch out for when working with numerical data. You also learned to write explanatory comments to make your code easier for you and others to read. Finally, you read about the philosophy of keeping your code as
simple as possible, whenever possible."
	In Chapter 3 you’ll learn to store collections of information in variables called lists. You’ll learn to work through a list, manipulating any information in that list.

 "In this chapter I learned a bit about Python in general, and I installed Python to my system. I will look to install a text editor to make it easier to write Python code. I learned to run snippets(small part) of Python code in a terminal session, and I ran my first actual program, hello_world.py. I probably learned a bit about troubleshooting as well.
 In the next chapter I’ll learn about the different kinds of data I can work with in my Python programs, and I’ll learn to use variables as well."

Summary_chapter_03:
	In this chapter you learned what lists are and how to work with the individual items in a list. You learned how to define a list and how to add and remove elements. You learned to sort lists permanently and temporarily for display purposes. You also learned how to find the length of a list and how to avoid index errors when you’re working with lists.
	In Chapter 4 you’ll learn how to work with items in a list more effi- ciently. By looping through each item in a list using just a few lines of code you’ll be able to work efficiently, even when your list contains thousands or millions of items.

