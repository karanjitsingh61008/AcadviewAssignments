#Q1Find the length of tuples,Find the minimum elemnent of tuple,Find the max elemnt of tuple,finding product of element of tuple
tuple1=('karan',8,7,'simran')
print(len(tuple1))#finding length of tuple
tuple2=(1,2,3,4,5,6,9,8)
print(max(tuple2))#finding minimum element of tuple
print(min(tuple2)))#finding maximum element of tuple
def product(tuple3):
    #Calculates the product of a tuple
    prod = 1
    for x in tuple3:
        prod = prod * x
    return prod
tuple3=(1,2,3,4)
print(product(tuple3))

#sets
#create sets and perfom operations
x=int(input('enter a number'))
y=int(input('enter a number'))
z=int(input('enter a number'))
i=int(input('enter a number'))
q=int(input('enter a number'))
r=int(input('enter a number'))
s=int(input('enter a number'))
t=int(input('enter a number'))
sets1={x,y,z,i}
sets2={q,r,s,t}
print(sets1)
print(sets2)                                                                
print(sets1-sets2)#difference
print(sets1 & sets2)#intersection of sets






#Dictionaries
#QCreate a dictionary to store name and marks of 10 students by user input and sort them. 
a=input('enter a name')#student 1
k=int(input('enter marks'))#student 1 marks
b=input('enter a name')#student 2
l=int(input('enter marks'))#student 1 marks
c=input('enter a name')#student 3
m=int(input('enter marks'))#student 3 marks
d=input('enter a name')#student 4
n=int(input('enter marks'))#student 4 marks and vice versa
e=input('enter a name')
o=int(input('enter marks'))
f=input('enter a name')
p=int(input('enter marks'))
g=input('enter a name')
q=int(input('enter marks'))
h=input('enter a name')
r=int(input('enter marks'))
i=input('enter a name')
s=int(input('enter marks'))
j=input('enter a name')
t=int(input('enter marks'))
mydict={a:k,b:l,c:m,d:n,e:o,f:p,g:q,h:r,i:s,j:t}
print(mydict)
print(mydict.sorted())#sorting the dicstionary
#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.
x='MISSISSIPPI'
y=(x.count('M'))#counting the no of times each word is repeated
z=(x.count('I'))
l=(x.count('S'))
e=(x.count('P'))
mydict1={'M':y,'I':z,'S':l,'P':e}#storing in dictionary
print(mydict1)











