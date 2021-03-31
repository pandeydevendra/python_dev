	
	>>Function:
		>>>Method:
			Cases: lower(), upper() and title()
		>>>Whitespace:
			"\t" , "\n" and "\n\t"
		>>>Strip:
			rstrip(), lstrip() and strip()
	>>Variable:
	>>String:
	>> Numbers:
		Integers, Floats and Complex
interconvertibles:
		string>> str = str(any number) = str(integer,float or complex)
		Integer>> int = int(string) = int(any words, letters)




>>>VARIABLES: Naming and Using Variables

	•Variable names can contain only letters(a-z), numbers(0-9), and underscores(_)
	•They can start with a letter or an underscore, but not with a number;viz: message_1 but not 1_message.
	•Spaces( ) are not allowed in variable names, but underscores(_) can be used to separate words in variable names. For example, greeting_message works, but greeting message will cause errors.
	•Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular pro-
grammatic purpose, such as the word print . (See “Python Keywordsand Built-in Functions” on page 489.)
	•Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length is better
than length_of_persons_name.
	.Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

Note:
	The Python variables you’re using at this point should be lowercase. You won’t get errors if you use uppercase letters, but it’s a good idea to avoid using them for now.
@Avoiding Name Errors When Using Variables:
					Every programmer makes mistakes, and most make mistakes every day. Although good programmers might create errors, they also know how to respond to those errors efficiently.

>>>STRINGS: 
	A string is simply a series of characters. Anything(numbers, alphabets, words etc) inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:
"This is a string."
'This is also a string.'
	This flexibility allows you to use quotes and apostrophes within your strings:
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community

>>To open terminal directly: ctrl - alt -T
>>To leave the Python prompt and return to a terminal prompt: ctrl -D or enter exit()
>>To change working directory(folder): cd ....(folder name)
>>To know about present directory: pwd
>>To see all list in the present directory: ls

Summary_chapter_01: 
	"In this chapter I learned a bit about Python in general, and I installed
Python to my system. I will look to install a text editor to make it easier to write Python code. I learned to run snippets(small part) of Python code in a terminal session, and I ran my first actual program,hello_world.py. I probably learned a bit about troubleshooting as well.
	In the next chapter I’ll learn about the different kinds of data I can work with in my Python programs, and I’ll learn to use variables as well."

Summary_chapter_02:
	"In this chapter you learned to work with variables. You learned to use descriptive variable names and how to resolve name errors and syn- tax errors when they arise. You learned what strings are and how to display strings using lowercase, uppercase, and titlecase. You started using whitespace to organize output neatly, and you learned to strip unneeded whitespace from different parts of a string. You started working
with integers and floats, and you read about some unexpected behavior to watch out for when working with numerical data. You also learned to write explanatory comments to make your code easier for you and others to read. Finally, you read about the philosophy of keeping your code as
simple as possible, whenever possible.
	In Chapter 3 you’ll learn to store collections of information in variables called lists. You’ll learn to work through a list, manipulating any information in that list.
