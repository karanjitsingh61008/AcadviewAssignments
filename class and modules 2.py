#Q1
class Animal:
    def __init__(self,eyes,legs):
        self.tigereyes=eyes
        self.tigerlegs=legs
    def animal_attribute(self):
        return print('Tiger has',self.tigereyes,'eyes and',self.tigerlegs,'legs')
class Tiger(Animal):
    pass
tigerobj=Tiger(2,4)
print(tigerobj.animal_attribute())

#Q2
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())#output is A,B 
print(a.g(), b.g())#output is A,B


#Q3
class Cop:
    def __init__(self,name,age,workexperience,designation):
        self.wname=name
        self.wage=age
        self.wexperience=workexperience
        self.wdesignation=designation
    def add(self):
        self.wname=input("Enter cop's name")
        self.wage=input("Enter cop's age")
        self.wexperience=input('work experience is')
        self.wdesignation=input('Designation of cop is')    
    
    def display(self):
        return print('Cop name  is',self.wname,'\nCopa age  is',self.wage,'\nWork esxperience is',self.wexperience,'yrs','\nDesignation is',self.wdesignation)
    def update(self):
        self.wname=input("Enter cop's name")
        self.wage=input("Enter cop's age")
        self.wexperience=input('work experience is')
        self.wdesignation=input('Designation of cop is')
        return print('Cop name  is',self.wname,'\nCopa age  is',self.wage,'\nWork esxperience is',self.wexperience,'yrs','\nDesignation is',self.wdesignation)
    

class Mission(Cop):
    def add_mission_details(self,newmission=Cop('karan','22','5','seniorofficer')):
        newmission.add()
        newmission.display()
        newmission.update()
obj1=Mission('karan','22','5','seniorofficer')
print(obj1.add_mission_details())
        






#Q4
class Shape:
    length=5
    breadth=4
    def area(self):
        return self.length*self.breadth
class Square(Shape):
    length=5
    breadth=5
class Rectangle(Shape):
    length=6
    breadth=5
squareobj=Square()
rectangleobj=Rectangle()
print(squareobj.area())
print(rectangleobj.area())    

                      
                      
