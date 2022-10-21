
import tkinter as tk
import tkinter.ttk
from datetime import datetime, timedelta



onespace = " "
longspace = "                                                         "
shortspace = "       "
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

def strf_interval(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{} {}{}'.format(
            "" if int(days) == 0 else str(int(days)) + 'd',#days
            "" if int(hours) == 0 else str(int(hours)) + 'h',#hours
            "" if int(minutes) == 0 else str(int(minutes))  + 'm' # mins
            #,"" if int(seconds) == 0 else str(int(seconds))  + ' secs'
        )


def dictionary():   
    for data1 in name:
        for data2 in var1:
            res[data1] = data2
            break

def countline():
    count=0
    with open(r"D:\Largecodefile\Customer.txt", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count+1

def appendlist():
    global var1
    var1=[]
    for i in range (0,int(countline()/2)):
        var1.append(0)


class readandwrite:
    def calculation(h): 
        if h =="(add value)":
            return 'Need val'
        else:
            date_object =datetime.strptime( h, '%m/%d/%y %H:%M')
            date_object2 = datetime.now()
            date= timedelta.total_seconds(date_object - date_object2)
            return strf_interval(date)

    def removal(i):
        if countline() >2:
            with open(r"D:\Largecodefile\Customer.txt", "r") as f:
                lines = f.readlines()
            h,j = i-2,i-1
            with open(r"D:\Largecodefile\Customer.txt", "w") as f:
                for i in range(0,2):
                    f.seek(0)
                    count=0
                    for line in lines:
                        if count != j and count != h:
                            f.write(line)
                        count+=1
            print(countline())                   
            readandwrite.striplastline()
        else:
            with open(r"D:\Largecodefile\Customer.txt", 'r+', encoding='utf-8') as update_new_proxies_file:
                update_new_proxies_file.truncate(0)

    def removals(i):
        with open(r"D:\Largecodefile\Customer.txt", 'r+', newline='') as f:
            lines = f.read().splitlines()
            h, j = i-2, i-1
            # validation here is critical
            if h >= 0 and j < len(lines):
                data1, data2 = lines[h], lines[j]
                f.seek(0) # BOF
                for line in lines:
                    if not line in {data1, data2}:
                        print(line, file=f) # print will add the newline
                f.truncate()
        readandwrite.striplastline()

    def striplastline():   
        with open(r"D:\Largecodefile\Customer.txt", "r") as f:
            lines = f.readlines() 
        data = lines[-1].strip('\n')
        lines[-1] = data
        with open(r"D:\Largecodefile\Customer.txt", "w") as f:
            f.writelines(lines)

    def addval():
        file = open(r"D:\Largecodefile\Customer.txt", 'a')
        if countline() >1:
            file.write(f"\n{text1.get()}\n(add value)")
        else:
            file.write(f"{text1.get()}\n(add value)")
        file.close()

    def typein(h):
        #print("**********h is ",h)
        with open(r"D:\Largecodefile\Customer.txt", 'r', encoding='utf-8') as file:
            data = file.readlines()

        #print('text get is',text.get())
        if h-1 == len(data)-1:
            data[h-1] = f"{text.get()}"#1 problem here, proably items or list length again
        else:
            data[h-1] = f"{text.get()}\n"

        with open(r"D:\Largecodefile\Customer.txt", 'w', encoding='utf-8') as file:
            file.writelines(data)
        file.close()
        

    def readday():
        global count
        global item
        item=0##responsible for incrementing list value
        ######selected = []  UNMARK THIS TO TUNR THINGS TO NORMAL
        
        appendlist()
        file1 = open(r"D:\Largecodefile\Customer.txt", 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            global frame
            global x
            global y
            count += 1#append item in lista against since that'd cause index bug
            #print("Line{}: {}".format(count, line.strip()))#format print :count: number , line.strip() : Line details
            horizontal.customize(line.strip(),1)
            horizontal.longspace(1)
            horizontal.smallspace(1)
            if oddseparator(count) == False:#already modified oddseparator and take out num!=1 for this
                horizontal.checkbox(1,count-1)#horizontal.smallspace()
            horizontal.smallspace(1)
            if (oddseparator(count)) == True: #can change this to oddseparator function (and num != 1)
                y+=1;horizontal.separator(1);y+=1;x=0
            #print(oddseparator(count),line.strip(),x,y) 

    def readday1():
        global count
        global item
        item=0##responsible for incrementing list value
        ######selected = []  UNMARK THIS TO TUNR THINGS TO NORMAL
        
        appendlist()
        file1 = open(r"D:\Largecodefile\Customer.txt", 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            global frame
            global x
            global y
            count += 1#append item in lista against since that'd cause index bug
            #print("Line{}: {}".format(count, line.strip()))#format print :count: number , line.strip() : Line details
            if (oddseparator(count)) == True:
                horizontal.customize(readandwrite.calculation(line.strip()),2)
            else: 
                horizontal.customize(line.strip(),1)
            horizontal.longspace(1)
            horizontal.smallspace(1)
            if oddseparator(count) == False:#already modified oddseparator and take out num!=1 for this
                horizontal.checkbox(1,count-1)#horizontal.smallspace()
            horizontal.smallspace(1)
            if (oddseparator(count)) == True: #can change this to oddseparator function (and num != 1)
                y+=1;horizontal.separator(1);y+=1;x=0
            #print(oddseparator(count),line.strip(),x,y)           


#function for command or additional properties
class fun():
    def calculate():
        frame.destroy()
        run1()

    def removing():
        #global selected
        count=0
        listdel = []
        for i in range (0,len(selected)):
            print('count as',count)
            if selected[i].get() == 1:
                listdel.append(i)
                val=(i-count+1)*2
                readandwrite.removal(val)
                count +=1
                #remove 1 value from list and startted scanning i at the same location( since already removed 1 check button value)
        #count = 0
        #for j in range (0,len(listdel)):
        #    print('selected is',selected)   #BUG DETECTED, GOTTA MOVE ALL THE KEYNAME UP 1 VALUE
        #                                    #print('listdel - count at',listdel[j]-count)#This logic is supposed to delete same value twice in order to calculate the step up, but in reality it actually delete 2,3
        #                                    #print(listdel)
        #    del selected[listdel[j]]         #definetly cause problem for 2 value and above if use listdel[i]-count for calculating the step up
        #    count+=1                         #this is because listdel will leave that index blank until we finished the calculation
        #                                    #selected = {} #already perfectly re declared things but need further monitor
        frame.destroy()
        run()


    def add():
        if len(text1.get()) !=0:
            if len(text1.get()) > 10:
                text1.delete(10,tk.END)
            readandwrite.addval()
            frame.destroy()
            run()
    def replace():
        if len(text.get()) != 0:
            if len(text.get()) > 14:
                text.delete(14,tk.END)
            elif len(text.get()) < 13:
                return
                #print('selected is',len(selected))#need to fix current selected took old values
                #print('item is ',item)
            for i in range (0,len(selected)):
                #print('i currently is ',i,'and list length', len(selected))
                if selected[i].get() == 1:
                    val=(i+1)*2
                    readandwrite.typein(val)   
        frame.destroy()          
        run()

            #if len(customize) < 14 and (No White Space, change bg or fg to red)

class horizontal:
    def customize(h,z):
        global x
        global custom
        if z == 2 and ("d" in h)== False:#len(h) < 7:
            custom=tk.Label(frame,fg='red', text = h, pady = 10,padx=10)
            custom.grid(row = y ,column = x);x+=1
        else:
            custom=tk.Label(frame, text = h, pady = 10,padx=10)
            custom.grid(row = y ,column = x);x+=1
    def longspace(z):
        global x
        if z ==0:
            tk.Label(root, text = longspace).grid(row = y ,column = x);x+=1
        if z ==1:
            tk.Label(frame, text = longspace).grid(row = y ,column = x);x+=1

    def smallspace(z):
        global x
        if z ==0:
            tk.Label(root, text = shortspace).grid(row = y ,column = x);x+=1
        if z ==1:
            tk.Label(frame, text = shortspace).grid(row = y ,column = x);x+=1

    
    def entry(z):
        global x
        global text
        if z==0:
            text=tk.Entry()
            text.grid(row = y ,column = x);x+=1
        if z == 1:
            text=tk.Entry(frame)
            text.grid(row = y ,column = x);x+=1
    

    def checkbox(z,i):
        global item
        global x
        global var1
        global selected
        if z == 0:
            is_var1 = tk.IntVar()
            tk.Checkbutton(root, text='Date change',variable=is_var1, onvalue=1, offvalue=0).grid(row = y ,column = x);x+=1
            selected[item]=is_var1
            item+=1
        if z== 1:
            is_var1 = tk.IntVar()
            tk.Checkbutton(frame, text='Date change',variable=is_var1, onvalue=1, offvalue=0).grid(row = y ,column = x);x+=1
            selected[item]=is_var1
            item+=1

    def separator(z):
        global x
        if z ==0:
            tkinter.ttk.Separator(root, orient='horizontal').grid(row=y, columnspan=72, sticky=tk.EW);x+1
        if z ==1:
            tkinter.ttk.Separator(frame, orient='horizontal').grid(row=y, columnspan=72, sticky=tk.EW);x+1



root = tk.Tk()
root.geometry('525x550')
root.resizable(False, False)
root.configure(bg="#e6f2ee")
root.title('Life Changer')



#row1***
x=1
y=0

Label1 = tk.Label(root, text = " Deadline Warner!!! ", bg="grey", fg="white")
Label1.grid(row = 0 ,column = 0)

horizontal.longspace(0)
horizontal.entry(0)                                                   
buttons = tk.Button(root,text="Change time" ,foreground="red", bg="white",padx=-10, pady=2, command=fun.replace).grid(row = y ,column = x);x+=1 # change all time on the box after click, can set time by radio button, each section should have one tick
#calculate needed horzontaline
num= len(Label1.cget('text')+longspace+shortspace)
#calculate needed horzontaline


#row2***
x=0
y=1

horizontal.separator(0)

#row3***
x=0;y=2
text1=tk.Entry()
text1.grid(row = y ,column = x);x+=1
tk.Button(root,text="Add details" ,foreground="red", bg="white",padx=40, pady=2, command=fun.add).grid(row = y ,column = x);x+=1
#tk.Radiobutton(text="Add details" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1
#tk.Radiobutton(text="Remove details" ,foreground="red", bg="white").grid(row = y ,column = x);x+=1
tk.Button(root,text="Remove details" ,foreground="red", bg="white",padx=20, pady=2, command= fun.removing).grid(row = y ,column = x);x+=1
tk.Button(root,text="Format" ,foreground="red", bg="white",padx= 5, pady=2, command = fun.calculate).grid(row = y ,column = x);x+=1
#row4***
x=0;y=3
horizontal.separator(0)

#row5***
x=0;y=4
def run():
    global frame
    global selected
    selected = {}
    x=0;y=4
    frame= tk.Frame(root)
    frame.grid(rowspan=100,columnspan = 72, sticky=tk.NSEW) 
    readandwrite.readday()
def run1():
    global frame
    global selected
    selected = {}
    x=0;y=4
    frame= tk.Frame(root)
    frame.grid(rowspan=100,columnspan = 72, sticky=tk.NSEW) 
    readandwrite.readday1()
run()


root.mainloop()
