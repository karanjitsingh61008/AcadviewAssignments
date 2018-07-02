#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class
class Circle:
    def __init__(self,radius):
        self.circleradius=radius
        
    def getArea(self):
        return 3.14*self.circleradius*self.circleradius
    def  getCircumference(self):
        return 2*3.14*self.circleradius
obj_circle=Circle(5)
print(obj_circle.getArea())
print(obj_circle.getCircumference())




#Q2 Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student
class Student:
    def __init__(self,name,rollnumber):
        self.studentname=name
        self.studentrollnumber=rollnumber
    def display(self):
        return self.studentname,self.studentrollnumber
Student1=Student('Name=karan','Rollno=1')
Student2=Student('Name=simran','Rollno=2')
print(Student1.display())
print(Student2.display())






#Q3 Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius. 
class Temperature:
    def __init__(self,fertemp,celtemp):
        self.fahrenheittemp=fertemp
        self.celsiustemp=celtemp
    def convertFahrenheit(self):
        return self.celsiustemp*1.8+32
    def convertCelsius(self):
        return  (self.fahrenheittemp-32)%1.8
obj1=Temperature(32,32)
print('this is conversion of celsius into farhenheit',obj1.convertFahrenheit())
print('this is conversion of farhenheit into celsius',obj1.convertCelsius())



#Q4
class MovieDetails:
    def __init__(self,Moviename,Artistname,Yearofrelease,Ratings):
        self.movie=Moviename
        self.artist=Artistname
        self.year=Yearofrelease
        self.rating=Ratings
    
    def display(self):
        return print('movie name is',self.movie,'\nartist name is',self.artist,'\nyear  of release is',self.year,'\nrating of movie is',self.rating)
    def update(self):
        self.movie=input('Enter movie name')
        self.artist=input('Enter artist name')
        self.year=input('Enter date of relase')
        self.rating=input('enter ratings')
        return  print('movie name is',self.movie,'\nartist name is',self.artist,'\nyear  of release is',self.year,'\nrating of movie is',self.rating) 
    
objdisplay=MovieDetails('Titanic','Leonardo','1998','4 star')
print(objdisplay.display())
print(objdisplay.update())


    
    




      
