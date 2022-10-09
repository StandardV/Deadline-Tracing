#deadline count down input and set time by user

#there should be one button set time and 1 button to assign that time either to 1 or all objects

# have a big client, can be connected in web

#should check if javascript can parse python in here and show in web

#sorting option to put all of the closest deadline together or group it by user choic

#should have a time counterdown next to the object, can hide or show it, mostly show by day

import tkinter as tk
import tkinter.ttk
import time
from turtle import window_height

onespace = " "
longspace = "                                                                                    "
shortspace = "        "
x = 0

class horizontal:
    def longspace():
        global x
        tk.Label(root, text = longspace).grid(row = y ,column = x);x+=1

    def smallspace():
        global x
        tk.Label(root, text = shortspace).grid(row = y ,column = x);x+=1
    
    def entry():
        global x
        tk.Entry().grid(row = y ,column = x);x+=1

    def separator():
        global x
        tkinter.ttk.Separator(root, orient='horizontal').grid(row=y, columnspan=10, sticky=tk.EW);x+1


root = tk.Tk()
root.resizable(False, False)
root.configure(bg="#e6f2ee")

#row1***
x=1
y=0
print(root)

Label1 = tk.Label(root, text = " Deadline Warner!!! ", bg="grey", fg="white")
Label1.grid(row = 0 ,column = 0)

horizontal.longspace()
horizontal.entry()                                                   
buttons = tk.Button(text="Change time" ,foreground="red", bg="white", pady=2).grid(row = y ,column = x);x+=1 # change all time on the box after click, can set time by radio button, each section should have one tick
horizontal.smallspace()
#calculate needed horzontaline
num= len(Label1.cget('text')+longspace+shortspace)
#calculate needed horzontaline


#row2***
x=0
y=1

horizontal.separator()

#row3***
x=0;y=2

horizontal.entry()
tk.Radiobutton(text="Change time" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1
tk.Radiobutton(text="Change time" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1

#row4***
x=0;y=3
horizontal.separator()

#row5***
x=0;y=4
horizontal.entry()


root.mainloop()

