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

# Text mode -->> r, w, a, r+, w+, a+, x;;;;; 7 modes

r = read only; <--> f = open('file.txt', 'r')
Error >> "FileNotFoundError" in case if the file does not exist 

w = write only; <--> f = open('file.txt', 'w') << It erases all previous data, writes new ones.
Error >> "No Error" in case if the file does not exist RATHER it creates a new empty file

a = append; No reading; only write; without erasing previous data.<--> f = open('file.txt', 'a')
Error >> "No Error" in case if the file does not exist RATHER it creates a new empty file

r+ = read and write from start <--> f = open('file.txt', 'r+')
     It is most commonly used to modify the file.
Error >> "FileNotFoundError" in case if the file does not exist 

w+ = read and write; It erases all previous data.; <--> f = open('file.txt', 'w+') 
Error >> "No Error" in case if the file does not exist RATHER it creates a new empty file

a+ = read and write; without erasing previous data.<--> f = open('file.txt', 'a+')
Error >> "No Error" in case if the file does not exist RATHER it creates a new empty file

x = exclusive write mode.<--> f = open('file.txt', 'x') ; 
    Fresh Writing; Always creates new file..
Error >> "FileAlreadyExistError" in case if the file already exists

# Binary Modes: textmode with b at last-->> rb, wb, ab, r+b, w+b, a+b, xb :: 7 modes

