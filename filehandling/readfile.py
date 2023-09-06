'''
File handling in Python is a powerful and versatile tool that can be used to perform a wide range of operations. However, it is important to carefully consider the advantages and disadvantages of file handling when writing Python programs, to ensure that the code is secure, reliable, and performs well.

Python File Handling
Python too supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, but like other concepts of Python, this concept here is also easy and short. Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun. Let’s start with the reading and writing files.

Advantages of File Handling
Versatility: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
Flexibility: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).
User–friendly: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
Cross-platform: Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.
Disadvantages of File Handling
Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
Security risks: File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
Complexity: File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
Performance: File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.
For this article, we will consider the following “geeks.txt” file as an example.

Hello world
GeeksforGeeks
123 456
Working of open() Function in Python
Before performing any operation on the file like reading or writing, first, we have to open that file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

f = open(filename, mode)
Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
 r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
Working in Read mode
There is more than one way to read a file in Python. Let us see how we can read the content of a file in read mode.

Example 1: The open command will open the file in the read mode and the for loop will print each line present in the file.
'''



# a file named "Test", will be opened with the reading mode.
file = open('Test.txt', 'r')

# This will print every line one by one in the file
for each in file:
	print (each)

# Python code to illustrate read() mode
file = open("Test.txt", "r")
print (file.read())

# Python code to illustrate with()
with open("Test.txt") as file:
    data = file.read()

print(data)


# Python code to illustrate read() mode character wise for fisrt 5 character
file = open("Test.txt", "r")
print (file.read(5))



# Python code to illustrate split() function
with open("split.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

