#Q1print something on screen
print('hello')

#Q2Join two strings 
s = "Acad"
v = "view"
print(s+v)

#Q3Take the input of 3 variables x, y and z . Print their values on screen. 
x=int(input('enter the number'))#first variable
y=int(input('enter the number'))#second variable
z=int(input('enter the number'))#third variable
print(x,y,z)

#Q4 Print “Let’s get started” on screen. 
print('“Let’s get started"') 

#Q5 Print the following values using placeholders.
s='acadview'
y="I'm doing python from %s"
print(y%s)#using placeholder 
course='python'
t='my course is %s'
print(t%course)
fees=500
z='my fees is %d'
print(z%fees)

#Q6 Fill in the blanks
name="TonyStark"
salary=1000000
print(("%s,%d")%(name,salary)) 
