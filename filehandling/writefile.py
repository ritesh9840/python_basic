'''
Creating a File using the write() Function
Just like reading a file in Python, there are a number of ways to write in a file in Python. Let us see how we can write the content of a file using the write() function in Python.

Working in Write Mode
Let’s see how to create a file and how the write mode works.

Example 1: In this example, we will see how the write mode and the write() function is used to write in a file. The close() command terminates all the resources in use and frees the system of this particular program.

'''



# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

    # Python code to illustrate append() mode
    file = open('geek.txt', 'a')
    file.write("This will add this line")
    file.close()