#Q1,Q2 Write a python program using tkinter interface to write Hello World and a exit button that closes the interface,
#create a action when the button is click it will display some text. 
import tkinter as Tk
def action():
     return print('hello man')
x=Tk.Tk()
var=Tk.StringVar()
yt=Tk.Label(x,textvariable=var)
var.set('hello world')
yt.pack()
bt=Tk.Button(x,text='exit',command=x.destroy)
bt.pack()
bt4=Tk.Button(x,text='action',command=action)
bt4.pack()
x.mainloop()

#Q3Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text. 
import tkinter as Tk
def changelabel():
    jas.config(text='hello')
x=Tk.Tk()
jas=Tk.Label(x, text="Old text")
jas.pack()
frame=Tk.Frame(x)
frame.pack()
frame2=Tk.Button(frame,text='change label',command=changelabel)
frame2.pack()
frame1=Tk.Button(frame,text='exit',command=x.destroy)
frame1.pack()
x.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it. 

import tkinter as Tk
def printtext():
    string = e.get() 
    print(string) 

x=Tk.Tk()
label=Tk.Label(x,text='your name').grid(row=0)
e=Tk.Entry(x,bd=5)
e.grid(row=0,column=1)
submit = Tk.Button(x, text ="Submit", command = printtext)
submit.grid(row=0,column=2)
x.mainloop()



