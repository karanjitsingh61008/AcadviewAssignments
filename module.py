#TIMETUPPLE
"""Return a time.struct_time such as returned by time.localtime(). d.timetuple() is equivalent to time.struct_time((d.year,d.month, d.day,d.hour,d.minute, d.second,
d.weekday(), yday, dst)),where yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1 is the day number within the current year starting with 1 for January 1st.
The tm_isdst flag of the result is set according to the dst() method: tzinfo is None or dst() returns None, tm_isdst is set to -1; else if dst() returns a non-zero
value, tm_isdst is set to 1; else tm_isdst is set to 0."""

#Q2,6 Write a program to get formatted time,Write a program to print time using localtime method. 
from datetime import datetime,timezone,timedelta
tday1=datetime.now()
print(tday1.strftime('%d-%m-%Y')) #using string format,local time method dd\mm\YYYY


#Q3,4,5Extract month from the time, Extract day from the time, Extract date from the time
import datetime
tday=datetime.date.today()
print(tday.month)#extracting month
print(tday.day)#extracting day
print(tday.weekday())#extracing the weekday


#Q7Find the factorial of a number input by user using math package functions
import math
x=int(input('enter a number'))
print(math.factorial(x))
#Q8Find the factorial of a number input by user using math package functions
y=int(input('enter a number'))
z=int(input('enter a number'))
print(math.gcd(y,z))



#Q9 getting current directory   
import os
cwd = os.getcwd()
print(cwd)
we=os.listdir()
print(we)

