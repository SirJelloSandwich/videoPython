#!/usr/bin/python

from Tkinter import *
import subprocess
import re

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def showWifi():
   output = subprocess.check_output(['sudo','wifi','scan'])
   kp = re.split('\n', output)
   var1.set( kp[0])
   var2.set(kp[1])



master = Tk()
master.geometry('500x300')

var=StringVar()
var1 = StringVar()
var2 = StringVar()
L = Label(master, textvariable = var1, relief=RAISED, width=40, anchor=W).place(x=100,y=20)
L1 = Label(master, textvariable = var2, relief=RAISED, width=40, anchor=W).place(x=100,y=40)
#Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
#e2 = Entry(master)

e1.place(x=150,y=150)
#e2.grid(row=1, column=1)




cb = Checkbutton(master, variable=var).place(x=50, y=20)

#Listbox1 = Listbox(master, width =50)
#Listbox1.grid(row=4, column=1)

#Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
B = Button(master, text='Wifi', command=showWifi)
B.place(x=200, y=200)
#Button(master, text='Show', command=show_entry_fields).grid(row=4, column=2, sticky=W, pady=4)


mainloop( )


