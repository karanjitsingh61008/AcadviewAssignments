#Q1
import pandas as pd

data={'Name':['karan','simran'],'Age':[21,22],'EmailId':['s.karanjit231@gmail.com','s.simranjit231@gmail.com'],'MobileNo':['8958237145','812345268']}
pd.DataFrame(data)
print(data)



#Q2
import pandas as pd
df=pd.read_csv('./weather.csv')
print(df.head(5))#First 5 rows
print(df.head(10))#First 10 rows
#c.) Find basic statistics on the particular dataset.
print(df['MinTemp'].describe())#Finding statistics
print(df['MaxTemp'].describe())#Finding statistics
print(df.tail(5))#Last 5 rows
print(df.loc[[1]])#printing specific location
init=df.loc[[1]]
            
