#File Handling in Python

# Python too supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files.
# Python treats file differently as text or binary and this is important.
# Each line of code includes a sequence of characters and they form text file.
# Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character.
# It ends the current line and tells the interpreter a new one has begun.

# File handling consists of four function:
# Create
# Read
# Update
# Delete

# Working of open() function

# We use open () function in Python to open a file in read or write mode.
# Open ( ) will return a file object. To return a file object we use open() function along with two arguments, that accepts file name and the mode, whether to read or write.
# So, the syntax being: open(filename, mode).
# These are the kinds of mode, that Python provides and how files can be opened:

# “ r “, for reading, returns an error, if the file doesn't exists.  --->default, if any mode is not being passed
# “ w “, for writing, creates the file if doesn't exist.
# “ a “, for appending, creates the file if doesn't exist.
# “ x “, for creating, returns an error, if the file exists.
# “ r+ “, for both reading and writing

# for file type, there is two option:
# 1> 't', for text files  --->default, if not any file type is passed
# 2> 'b', for binary files

# The open command will open the file in the read mode and the for loop will printeach line present in the file.
file = open('demo.txt', 'rt')
for line in file:
    print(line)
file.close()    # used to close thee file

# Working of read() mode
# to extract a string that contains all characters in the file then we can use file.read().
file = open('demo.txt', 'r')
print(file.read())
file.close()

# to call a certain number of characters
file = open('demo.txt', 'r')
print(file.read(10))    # read the first five characters of stored data and return it as a string
file.close()

# Reading teext file lines:

file = open('demo.txt', 'r')
print(file.readline())       # return 1st line by default
file.close()

file = open('demo.txt', 'r')
print(file.readline(5))       # Return only the first five bytes from the first line:
file.close()

file = open('demo.txt', 'r')
print(file.readline())       # Return the first line and 2nd line:
print(file.readline())
file.close()

file = open('demo.txt', 'r')
print(file.readlines())       # Read lines separately:
file.close()

# looping over a file object: to return each and every line in an eefficieent way

file = open('demo.txt', 'r')
for line in file:
    print(file.readlines())       # Return only the first five bytes from the first line:
file.close()

# Creating a file using write() mode
# in 'w' mode, it creates the file, if it's not there, if its already there, it overwrite the entire file
# Python code to create a file
file = open('demo2.txt','w')
file.write("What is Lorem Ipsum? \n")
file.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n")
file.write("It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n")
file.close()
# The close() command terminates all the resources in use and frees the system of this particular program.

# Working of append() mode  - in appeend modee, everything got appended in the file
# to Copy the Contents of One File into Another
file = open('demo.txt', 'a')
temp_file = open('demo2.txt', 'r')
for line in temp_file:
    file.write(line)
file.close()
temp_file.close()

# # to delete a file, import OS modulee and run its os.remove() function
# import os
# os.remove('demo3.txt')
#
# # Creating a file:
# file = open('demo3.txt','x')  # using 'x' mode, gives an error, if the file already exist i.e: FileExistsError: [Errno 17] File exists: 'demo3.txt'
# file.close()

# so, its a better option to check the file existence and remove it, before creating any file :
import os
if os.path.exists('demo3.txt'):
    os.remove('demo3.txt')
    file = open('demo3.txt', 'x')
    file.close()
else:
    file = open('demo3.txt', 'x')
    file.close()

# rstrip(): This function strips each line of a file off spaces from the right-hand side.
# lstrip(): This function strips each line of a file off spaces from the left-hand side.
# strip(): covers both rstrip and lstrip functionality
file = open('demo.txt', 'a')
temp_file = open('demo2.txt', 'r')
for line in temp_file:
    file.write(line.rstrip())
file.close()
temp_file.close()

# with() function: This is helpful because using this method any files opened will be closed automatically after one is done, so auto-cleanup.

with open("demo.txt") as file:
    data = file.read()
print(data)

# Using append along with with() function
with open('demo.txt','a') as file:
    file.write("\ngoing to finish with file handling")

# split() using file handling - We can also split lines using file handling in Python.
# This splits the variable when space is encountered. You can also split using any characters as we wish.

with open('demo2.txt','r') as file:
    for line in file:
        word = line.split()
        print(word)


#                    -------------------------------------------OUTPUT-------------------------------------------------           #
'''
    raushan@rk-ubuntu:~/Desktop/revising_python$ python3 file_handling.py 
Hello World!

This is Raushan Kumar.

I am revising python Currently.What is Lorem Ipsum? 

Lorem Ipsum is simply dummy text of the printing and typesetting industry.

It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

going to finish with file handling
Hello World!
This is Raushan Kumar.
I am revising python Currently.What is Lorem Ipsum? 
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
going to finish with file handling
Hello Worl
Hello World!

Hello
Hello World!

This is Raushan Kumar.

['Hello World!\n', 'This is Raushan Kumar.\n', 'I am revising python Currently.What is Lorem Ipsum? \n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n', 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n', 'What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n', 'going to finish with file handling']
['This is Raushan Kumar.\n', 'I am revising python Currently.What is Lorem Ipsum? \n', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n', 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n', 'What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n', 'going to finish with file handling']
Hello World!
This is Raushan Kumar.
I am revising python Currently.What is Lorem Ipsum? 
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
going to finish with file handlingWhat is Lorem Ipsum? 
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
What is Lorem Ipsum?Lorem Ipsum is simply dummy text of the printing and typesetting industry.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
['What', 'is', 'Lorem', 'Ipsum?']
['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.']
['It', 'has', 'survived', 'not', 'only', 'five', 'centuries,', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining', 'essentially', 'unchanged.']

'''