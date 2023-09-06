
'''
Timer is a sub class of Thread class defined in python. It is started by calling the start() function corresponding to the timer explicitly
'''

# Program to demonstrate
# timer objects in python

import threading


def gfg():
    print("GeeksforGeeks\n")


timer = threading.Timer(2.0, gfg)
timer.start()
print("Exit\n")