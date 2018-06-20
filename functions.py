#Q1 To find area of a circle
def SetArea ():
    radius = int(input('enter the radius'))
    myarea =3.14*radius** 2
    return myarea
print(SetArea())

#Q2 Finding perfect number
def perfect(x):
   list=[]
   for i in range(1,x ):#finding factors except number itself
       if x % i == 0:
           list.append(i)
   return list
x=int(input('enter a number'))
list2=[]
list3=[]
list2=perfect(x)
if sum(list2)==x: #condition for perfect number
   print('it is a perfect number')
   list3=x
   print('perfect number',list3)
else:
   print('it is not a perfect number')


#Q3Printing table of 12
def timetable(n, time=1):#here time tell the number we have to multiply our n with
    if time <= 10:
        print(n,'*',time,'=',n*time)
        timetable(n, time+1)
    else:
        return

timetable(12)

#Q4 Write a function to calculate power of a number raised to other ( a^b ) using recursion. 
def power(a,b):
    if b == 0:
       return 1
    if b >= 1:
        return a * power(a, b - 1)
print(power(a=int(input("enter the number")),b=int(input("enter the number"))))


#Q5 Write a function to find factorial of a number but also store the factorials calculated in a dictionary 
dict={}
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input('enter a number'))
dict['factorial']=factorial(n)   #storing factorial in dictionary
print(dict)
