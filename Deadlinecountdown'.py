from pickletools import read_float8
import tkinter as tk
import tkinter.ttk
import time
import sys
import fileinput

onespace = " "
longspace = "                                                                                    "
shortspace = "        "
x = 0
trash1 = 1
item=0


selected = {}
var1 = []
name = []
res = {}
count=0
#research
#https://www.geeksforgeeks.org/changing-the-colour-of-tkinter-menu-bar/ 
#https://stackoverflow.com/questions/23836000/can-i-change-the-title-bar-in-tkinter

def oddseparator(num):
    if (num%2) ==0 :
        return True
    else:
        return False

def dictionary():   
    for data1 in name:
        for data2 in var1:
            res[data1] = data2
            break

def countline():
    count=0
    with open("Customer.txt", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count+1

def appendlist():
    global var1
    for i in range (0,int(countline()/2)):
        var1.append(0)


class readandwrite:
    def typein(h):
        print("**********h is ",h)
        with open(r"D:\Largecodefile\Customer.txt", 'r', encoding='utf-8') as file:
            data = file.readlines()

        print('text get is',text.get())
        data[h-1] = "11-201\n"#text.get()

        with open(r"D:\Largecodefile\Customer.txt", 'w', encoding='utf-8') as file:
            file.writelines(data)

    def readday():
        global count
        appendlist()
        file1 = open(r"D:\Largecodefile\Customer.txt", 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            global x
            global y
            count += 1
            #print("Line{}: {}".format(count, line.strip()))#format print :count: number , line.strip() : Line details
            horizontal.customize(line.strip())
            horizontal.longspace()
            if oddseparator(count) == False:#already modified oddseparator and take out num!=1 for this
                horizontal.checkbox(count-1)#horizontal.smallspace()
            print(count)
            if (oddseparator(count) and num !=1) == True: #can change this to oddseparator function (and num != 1)
                y+=1;horizontal.separator();y+=1;x=0
            print(oddseparator(count),line.strip(),x,y)           


#function for command or additional properties
class fun():
    def writi():
        for i in range (0,len(selected)):
            if selected[i].get() == 1:
                print('huhuhhaha')
    def replace():
        for i in range (0,len(selected)):
            if selected[i].get() == 1:
                readandwrite.typein((i+1)*2)
            run()

            
    
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
        global text
        text=tk.Entry(root)
        text.grid(row = y ,column = x);x+=1
    
    def checkbox(i):
        global item
        global x
        global var1
        global selected
        is_var1 = tk.IntVar()
        tk.Checkbutton(root, text='Date change',variable=is_var1, onvalue=1, offvalue=0).grid(row = y ,column = x);x+=1
        selected[item]=is_var1
        item+=1

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
buttons = tk.Button(text="Change time" ,foreground="red", bg="white", pady=2, command=fun.replace).grid(row = y ,column = x);x+=1 # change all time on the box after click, can set time by radio button, each section should have one tick
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
def run():
    x=0;y=4
    readandwrite.readday()

run()


root.mainloop()

