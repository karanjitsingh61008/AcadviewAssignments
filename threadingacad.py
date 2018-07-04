#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.
import threading
import time

exitflag=0
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
         print('starting' + self.name)
         print_time(self.name,1,5)
         print('exiting' + self.name)

def print_time(threadname,counter,delay):
    while counter:
        if exitflag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s " % (threadname,time.ctime(time.time())))
        counter -= 1
KARAN=myThread('simran')
KARAN.start()




#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between
import threading
import time

exitflag=0
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
         print('starting' + self.name)
         print_time(self.name,10,1)
         print('exiting' + self.name)

def print_time(threadname,counter,delay):
    while counter:
        if exitflag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s " % ((11-counter),time.ctime(time.time())))
        counter -= 1
KARAN=myThread('simran')
KARAN.start()





#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec
import threading
import time

exitflag=0
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
         print('starting' + self.name)
         print_time(self.name,2)
         print('exiting' + self.name)

def print_time(threadname,delay):
    for i in range(0,5):
            if exitflag:
                threadname.exit()
            time.sleep(delay)
            print("%s: %s " % ((list[i]),time.ctime(time.time())))

list=['sim','dim','3','4','5']
KARAN=myThread('simran')
KARAN.start()


#Q4. Call factorial function using thread.

import threading
import time

class myThread(threading.Thread):
    def __init__(self,factnum):
        threading.Thread.__init__(self)
        self.factnum=factnum

    def run(self):
        import math
        math.factorial(self.factnum)
        print('%s:'%(self.factnum))


KARAN=myThread(int(input('enter a no')))
KARAN.start()