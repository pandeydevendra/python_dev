Data : Data are sequence of characters
File : File contains data
Files are of two type; text and binary
(i) Text File : It contains written information...; format >> file.txt, file.py, file.dat etc
(ii) Binary File : It contains binary information.. viz; file of image, audio and video  

No import is required 
Steps -->> :: create -> open -> process -> close

format;
file = open('filename', 'mode')::;

filename can be called/created by two means: 
         -->> current file ; eg: file_abc.txt
         -->> path:: provide path  ; eg D:\folder\file_xyz.txt

mode -->> r, w, a, r+, w+, a+, x;;;;; 7 modes
r = read only; <--> f = open('file.txt', 'r')
Error >> "FileNotFoundError" in case if the file does not exist 

w = write only; <--> f = open('file.txt', 'w')
Error >> "No Error" in case if the file does not exist RATHER it creates a new file

a
r
w
a
x