#Q1 Take 10 integers from user and print it on screen
x=0
list=[]
while x<=9:
    i=int(input('enter your number'))
    list.append(i)   
    print(list)
    x+=1
    




#Q2 Write an infinite loop
a=5
while a==5:
    print('hello')




#Q3Create a list of integer elements by user input.Make a new list which will store square of elements of previous list
LIST=[]
for i in range(5):
   i=int(input('enter a number'))
   LIST.append(i)
print(LIST)

newlist=[]
for j in LIST:
    newlist.append(j**2)
print(newlist)





#Q4From a list containing ints, strings and floats, make three lists to store them separately 
list=[1,4,8,'4','5',4.0]
intlist=[]
strlist=[]
floatlist=[]

for i in list:
   if isinstance(i,int):
      intlist.append(i)
      print('int list is',intlist)
   elif isinstance(i,str):
        strlist.append(i)
        print('string list is',strlist)
   else:
      floatlist.append(i)
      print('float list is',floatlist)
      




#Q5Using range(1,101), make a list containing even and odd numbers. 
LIST=[]
evenlist=[]
oddlist=[]
for i in range(1,101):
   LIST=[i]
   if i%2==0:
      evenlist.append(i)
      print('this is even list',evenlist)
   else:
      oddlist.append(i)
      print('this is odd list',oddlist)
      
      

#Q6 Print the pattern
for x in range(5):
    print('*'*x)



#Q7 Create a user defined dictionary and get keys corresponding to the value using for loop.
dict={}
for i in range(2):
    key=input('enter a name')
    keyvalue=int(input('enter a number'))
    dict[key]=keyvalue
print(dict)    
    


#Q8Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop. 

list=[]
for i in range(5):
   x=int(input('enter a number'))
   list.append(x)
   print(list)
searched_num=int(input('enter a number'))
if list[i]==searched_num:
      list.remove(searched_num)
      print(list)
else:  
      print(list)
   

    
      

   
       
    
