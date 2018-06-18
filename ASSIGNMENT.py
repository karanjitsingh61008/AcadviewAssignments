#Q1 Programme for calculatin Leap Year
Year=int(input('enter the year'))  #variable year is used to take input from user
if (Year%4==0):  #condition for a year to be leap year   
    if (Year%100==0): #checking if the year is century year or not
        if (Year%400==0): #condition for century years
            print('It is a leap year')
        else:
            print('It is not a leap year')
    else:
        print("It is a Leap Year")
else: #if condition resolves to false this block will be executed
               print('It is not a leap year')
                     






#Q2 To check whether the given dimension are of square or rectangle
length = int(input("enter  the length")) #taking first input from user
breadth  = int(input('enter the breadth')) #taking 2nd input from user
if (length==breadth): #if both the sides are equal it is a square
            print("it is a square")
else:
            print("it is a rectangle")



            



#Q3 Determine The Oldest And The Youngest People
person1=int(input('enter the age of person1'))
person2=int(input('enter the age of person 2'))
person3=int(input('enter the age of person3'))
if (person1>person2 and   person1>person3): #condition for person1 to be oldest
    print("person 1 is oldest")
elif (person2>person1 and person2>person3):  #condition for person2 to be oldest
    print("person 2 is oldest")
else:
    print('person 3 is oldest')
    
if (person1<person2 and   person1<person3):  #condition for person1 to youngest
    print("person 1 is youngest")
elif (person2<person1 and person2<person3):   #condition for person2 to be youngest
      print("person 2 is youngest")
else:
    print('person 3 is youngest')






#Q4 Write an if statement to lets competitor know which of these prises they won. 
points=int(input('enter the score'))
if (points<=50):
   print('sorry!no prize this time')
elif (points>50 and points<=150):
    print("Congratulations! You won a Wodden Dog")
elif (points>150 and points<=180):
    print("Congratulations! You won a Book")
elif (points>180 and points<=200):
    print("Congratulations! You won Chocolates")
else:
     Print("invalid score")
    







#Q5 Print Total Cost after getting discount
quantities=int(input('enter the quantity')) #no of quantities purchased
if (quantities*100>1000): #10% discount given if the condition is satisfied
    print('cost is ',((quantities*100)-(.1*quantities*100)))
else:
    print('cost is',quantities*100)
    
