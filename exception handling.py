#Q1Name and handle the exception occurred in the following program:
#error is zerodivisonerror
try:
    a=3
    if a<4:
      a=a/(a-3)
      print(a)

except ZeroDivisionError:
    print('error hai')



    

#Q2Name and handle the exception occurred in the following program:
#errror is index out of range    
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print('index is out of range')




   
  
#Q4 OUTPUT OF PROGRAMME  
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
AbyB(2.0,3.0)#OUTPUT IS -5.0
AbyB(3.0,3.0)#output is a/b result in 0







#Q3Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise
#OUTPUT NameError("Hi there")
    



#Q5
#Import Error
try:
    import __hello
    
except ImportError:
    raise ImportError("error ha")


#value error
def AbyB(a,b):
               c = ((a+b) / (a-b))
               print(c)
try:
    a=int(input('enter a number'))
except ValueError:
    print('Wrong value')
try:
    b=int(input('enter a number'))
except ValueError:
    print('Wrong value')          
AbyB(a,b)

#IndexError
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print('index is out of range')
    


#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#The code must keep taking input till the user enters the appropriate age number(less than 18).
class Error(Exception):
    pass
class AgeTooSmall(Error):
    pass
def main(): 
    while True:
         x=int(input('enter age'))
         try:
            if x<18:
                raise AgeTooSmall
         except AgeTooSmall:
            print('age is small')
         else:
            print('age is coreect')
            return
main()
        
    
       
    



             


