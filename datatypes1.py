#Q1,2,3 List using Input,Add to List,Count the number of time an object occurs in a list
a=input('enter a name')
b=input('enter a name')
c=input('enter a name')
list=['a','b','c']
print(list)
list2=['google','apple','facebook','microsoft','tesla']
print(list+list2)
print(list2.count('google'))#counting no of times google is there in list

#Q4- create a list with numbers and sort it in ascending order
list4=[1,9,10,5,6,11,7]
print(sorted(list4, key=int))

#Q5Merge 2 arrays into one
A=[1,8,7,6]
B=[55,42,58,4]
C=A+B
print(sorted(C, key=int))


#Q6Implementing stack and queue

stack=["karan", "simran", "harman"]#creating a stack
stack.append("hargun")#As it is lifo element adde to last place
stack.append("mansher")
print(stack)
print(stack.pop())#most recent elemnent added will be popped

#Importing the library
from collections import deque
#Creating a Queue
queue = deque([1,5,8,9])
#Enqueuing elements to the Queue
queue.append(7) #[1,5,8,9,7]
queue.append(0) #[1,5,8,9,7,0]
#Dequeuing elements from the Queue
queue.popleft() #[5,8,9,7,0]
queue.popleft() #[8,7,9,0]
#Printing the elements of the Queue
print(queue)
