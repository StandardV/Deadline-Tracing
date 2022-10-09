import tkinter as tk
import tkinter.ttk
import time
from turtle import window_height

onespace = " "
longspace = "                                                                                    "
shortspace = "        "
x = 0
#research
#https://www.geeksforgeeks.org/changing-the-colour-of-tkinter-menu-bar/ 
#https://stackoverflow.com/questions/23836000/can-i-change-the-title-bar-in-tkinter

def oddseparator(num):
    if (num%2) ==0 and num !=1 :
        return True
    else:
        return False

class readandwrite:
    def typein():#check for time condition if work first
        file1 = open('Customer.txt', 'w')
        file1.writelines(("Hello there"))
        file1.close()

    def readday():
        file1 = open('Customer.txt', 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            global x
            global y
            count += 1
            #print("Line{}: {}".format(count, line.strip()))#format print :count: number , line.strip() : Line details
            horizontal.customize(line.strip())
            horizontal.longspace();horizontal.smallspace()
            print(count)
            if oddseparator(count) == True:
                y+=1;horizontal.separator();y+=1;x=0
            print(oddseparator(count),line.strip(),x,y)           

    
class horizontal:
    def customize(h):
        global x
        tk.Label(root, text = h, pady = 10).grid(row = y ,column = x);x+=1
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
        tkinter.ttk.Separator(root, orient='horizontal').grid(row=y, columnspan=6, sticky=tk.EW);x+1


root = tk.Tk()
root.geometry('615x550')
root.resizable(False, False)
root.configure(bg="#e6f2ee")


#row1***
x=1
y=0

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
tk.Radiobutton(text="Add details" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1
tk.Radiobutton(text="Remove details" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1

#row4***
x=0;y=3
horizontal.separator()

#row5***
x=0;y=4
readandwrite.readday()

root.mainloop()

