import sqlite3
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
#Q1CREATING A TABLE
cursor.execute('CREATE TABLE IF NOT EXISTS  Books("Books Id" integer,"Title Id" integer,"Location text,Genre text)')
cursor.execute('CREATE TABLE IF NOT EXISTS   Titles(Title_Id integer,Title text,ISBN integer,Publisher_Id text,Publication Year integer)')
cursor.execute('CREATE TABLE IF NOT EXISTS   Publishers(Publisher Id integer,Zip Code Id integer,Suite Number integer,Name text,STREET Address text)')
cursor.execute('CREATE TABLE IF NOT EXISTS   ZipCodes(Zip_Code Id integer,ZipCode integer,State text,City text)')
cursor.execute('CREATE TABLE IF NOT EXISTS   AuthorTitles(Author_Title Id integer,Author Id integer,Title Id integer)')
cursor.execute('CREATE TABLE IF NOT EXISTS   Authors(Author Id integer,First Name text,Middle Name text,Last Name text)')
#Q2INSERTING VALUES IN TABLES
cursor.execute('INSERT INTO Books VALUES(453,671,"TOP SHELF","FICTIONAL")')
cursor.execute('INSERT INTO Titles VALUES(27,"batman",12,345,1998)')
cursor.execute('INSERT INTO Publishers VALUES(9,558,88,"gg martin","32-l")')               
cursor.execute('INSERT INTO ZipCodes VALUES(2,456,"PUNJAB","patiala")')
cursor.execute('INSERT INTO AuthorTitles VALUES(89,5,7)')
cursor.execute('INSERT INTO Authors VALUES(12,"GR","MARTIN","SINGH")')
cursor.execute('UPDATE Books SET Genre="HORROR"')#Q3WE HAVE OUR UPDATED VALUE
connection.commit()
connection.close()
connection=sqlite3.connect('data.db')
cursor=connection.cursor()
cursor.fetchall()

