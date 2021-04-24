from tkinter import *
import tkinter as tk
import sys
import os
from tkinter import messagebox

window = Tk()

window.title("BruteForcer")

window.geometry('700x300')

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()

var1.set(0)
var2.set(0)
var3.set(12)
var4.set(4)
#var5.set(0)

#### Labels ####
lbl = Label(window, text="Select Frequency")

lbl.grid(column=0, row=0)

lbl = Label(window, text="Select Baud Rate")

lbl.grid(column=1, row=0)

lbl = Label(window, text="Select BIT length")

lbl.grid(column=2, row=0)

lbl = Label(window, text="Select Repeating Times")

lbl.grid(column=3, row=0)

#### Callbacks ####

def disableEntry1():
    txt1.configure(state="disabled")
    txt1.update()

def enableEntry1():
    txt1.configure(state="normal")
    txt1.update()

#### ####

def disableEntry2():
    txt2.configure(state="disabled")
    txt2.update()

def enableEntry2():
    txt2.configure(state="normal")
    txt2.update()

#### ####

def disableEntry3():
    txt3.configure(state="disabled")
    txt3.update()

def enableEntry3():
    txt3.configure(state="normal")
    txt3.update()

#### ####

def disableEntry4():
    txt4.configure(state="disabled")
    txt4.update()


def enableEntry4():
    txt4.configure(state="normal")
    txt4.update()

#### Radio Buttons (Freq) ####

rad1 = Radiobutton(window,text='300 MHz', variable = var1, value=300000000, command=disableEntry1)

rad1.grid(column=0, row=2)

rad2 = Radiobutton(window,text='310 MHz', variable = var1, value=310000000, command=disableEntry1)

rad2.grid(column=0, row=3)

rad3 = Radiobutton(window,text='315 MHz', variable = var1, value=315000000, command=disableEntry1)

rad3.grid(column=0, row=4)

rad4 = Radiobutton(window,text='318 MHz', variable = var1, value=318000000, command=disableEntry1)

rad4.grid(column=0, row=5)

rad5 = Radiobutton(window,text='390 MHz', variable = var1, value=390000000, command=disableEntry1)

rad5.grid(column=0, row=6)

rad6 = Radiobutton(window,text='Custom', variable = var1, value="", command=enableEntry1)

txt1 = Entry(window,width=10, textvariable = var1, state="disabled")

txt1.grid(column=0, row=8)

rad6.grid(column=0, row=7)

#### Radio Buttons (Baud Rate) ####

rad7 = Radiobutton(window,text='1200', variable = var2, value=1200, command=disableEntry2)

rad7.grid(column=1, row=2)

rad8 = Radiobutton(window,text='2400', variable = var2, value=2400, command=disableEntry2)

rad8.grid(column=1, row=3)

rad9 = Radiobutton(window,text='4800', variable = var2, value=4800, command=disableEntry2)

rad9.grid(column=1, row=4)

rad10 = Radiobutton(window,text='Custom',variable = var2, command=enableEntry2)

txt2 = Entry(window,width=10, textvariable = var2, state="disabled")

txt2.grid(column=1, row=6)

rad10.grid(column=1, row=5)
#### Selecting BIT length ####

rad11 = Radiobutton(window,text='8', variable = var3, value=8, command=disableEntry3)

rad11.grid(column=2, row=2, padx=50, pady = 5)

###############

rad12 = Radiobutton(window,text='9', variable = var3, value=9, command=disableEntry3)

rad12.grid(column=2, row=3)

###############

rad13 = Radiobutton(window,text='10', variable = var3, value=10, command=disableEntry3)

rad13.grid(column=2, row=4)

###############

rad14 = Radiobutton(window,text='11', variable = var3, value=11, command=disableEntry3)

rad14.grid(column=2, row=5)

###############

rad15 = Radiobutton(window,text='12', variable = var3, value=12, command=disableEntry3)

rad15.grid(column=2, row=6)

###############

rad16 = Radiobutton(window,text='Custom', variable = var3, value="", command=enableEntry3)
#mystring =tk.StringVar(window)
txt3 = Entry(window, textvariable = var3, width=10, state='disabled')

txt3.grid(column=2, row=8)

rad16.grid(column=2, row=7)

#### Radio Buttons (Repeating Time) ####

rad17 = Radiobutton(window,text='2', variable = var4, value=2, command=disableEntry4)

rad17.grid(column=3, row=2)

###############

rad18 = Radiobutton(window,text='4', variable = var4, value=4, command=disableEntry4)

rad18.grid(column=3, row=3)

###############

rad19 = Radiobutton(window,text='6', variable = var4, value=6, command=disableEntry4)

rad19.grid(column=3, row=4)

###############

rad20 = Radiobutton(window,text='Custom', variable = var4, value="", command=enableEntry4)
#mystring =tk.StringVar(window)
txt4 = Entry(window, textvariable = var4, width=10, state='disabled')

txt4.grid(column=3, row=6)

rad20.grid(column=3, row=5)

#### Execution ####

#var2 = var5

#### Modes ####
def Selected():

        os.system('sudo python3 rfpwnon.py -f ' + str(var1.get()) + ' -b ' + str (var2.get()) + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

def DebSeq():

        os.system('sudo python3 rfpwnon.py -f ' + str(var1.get()) + ' -b ' + str (var2.get()) + ' -l ' + str (var3.get()))

def BruteAll():
        tt = Tk()

        tt.title("BruteForcer")
        tt.configure(background='black')

        tt.geometry('480x330')

        #### 300 - 1200 ####
        lbl = Label(tt, text="Transmitting on Frequency: 300Mhz, With Baud Rate of: 1200...", fg ="green", bg="black").grid(column=0, row=0)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 300000000 -b 1200' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 300 - 2400 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=0)
        lbl = Label(tt, text="Transmitting on Frequency: 300Mhz, With Baud Rate of: 2400...", fg ="green", bg="black").grid(column=0, row=1)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 300000000 -b 2400' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))
        #lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=0)

        #### 300 - 4800 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=1)
        lbl = Label(tt, text="Transmitting on Frequency: 300Mhz, With Baud Rate of: 4800...", fg ="green", bg="black").grid(column=0, row=2)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 300000000 -b 4800' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))
        #lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=1)

        #### 310 - 1200 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=2)
        lbl = Label(tt, text="Transmitting on Frequency: 310Mhz, With Baud Rate of: 1200...", fg ="green", bg="black").grid(column=0, row=3)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 310000000 -b 1200' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 310 - 2400 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=3)
        lbl = Label(tt, text="Transmitting on Frequency: 310Mhz, With Baud Rate of: 2400...", fg ="green", bg="black").grid(column=0, row=4)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 310000000 -b 2400' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 310 - 4800 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=4)
        lbl = Label(tt, text="Transmitting on Frequency: 310Mhz, With Baud Rate of: 4800...", fg ="green", bg="black").grid(column=0, row=5)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 310000000 -b 4800' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 315 - 1200 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=5)
        lbl = Label(tt, text="Transmitting on Frequency: 315Mhz, With Baud Rate of: 1200...", fg ="green", bg="black").grid(column=0, row=6)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 315000000 -b 1200' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 315 - 2400 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=6)
        lbl = Label(tt, text="Transmitting on Frequency: 315Mhz, With Baud Rate of: 2400...", fg ="green", bg="black").grid(column=0, row=7)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 315000000 -b 2400' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 315 - 4800 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=7)
        lbl = Label(tt, text="Transmitting on Frequency: 315Mhz, With Baud Rate of: 4800...", fg ="green", bg="black").grid(column=0, row=8)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 315000000 -b 4800' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 318 - 1200 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=8)
        lbl = Label(tt, text="Transmitting on Frequency: 318Mhz, With Baud Rate of: 1200...", fg ="green", bg="black").grid(column=0, row=9)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 318000000 -b 1200' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 318 - 2400 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=9)
        lbl = Label(tt, text="Transmitting on Frequency: 318Mhz, With Baud Rate of: 2400...", fg ="green", bg="black").grid(column=0, row=10)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 318000000 -b 2400' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 318 - 4800 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=10)
        lbl = Label(tt, text="Transmitting on Frequency: 318Mhz, With Baud Rate of: 4800...", fg ="green", bg="black").grid(column=0, row=11)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 318000000 -b 4800' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 390 - 1200 ####
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=11)
        lbl = Label(tt, text="Transmitting on Frequency: 390Mhz, With Baud Rate of: 1200...", fg ="green", bg="black").grid(column=0, row=12)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 390000000 -b 1200' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 390 - 2400 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=12)
        lbl = Label(tt, text="Transmitting on Frequency: 390Mhz, With Baud Rate of: 2400...", fg ="green", bg="black").grid(column=0, row=13)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 390000000 -b 2400' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))

        #### 390 - 4800 ####
        lbl = Label(tt, text="Done", fg ="green", bg="black").grid(column=1, row=13)
        lbl = Label(tt, text="Transmitting on Frequency: 390Mhz, With Baud Rate of: 4800...", fg ="green", bg="black").grid(column=0, row=14)
        tt.update_idletasks()
        tt.update()
        os.system('sudo python3 rfpwnonall.py -f 390000000 -b 4800' + ' -l ' + str (var3.get()) + ' -r' + str(var4.get()))
        lbl = Label(tt, text="Done", fg="green", bg="black").grid(column=1, row=14)
        tt.update_idletasks()
        tt.update()

        tt.mainloop()



#### Buttons ####
btn1 = Button(window, text="Brute Force", command=Selected).grid(column=0, row=9)

btn2 = Button(window, text="Brute Everything", bg = "red", command=BruteAll).grid(column=1, row=9)

lbl1 = Label(window, text="Made By Abdullah Alawdan")

lbl1.grid(column=0, row=10, pady = 60)

#### End ####

window.mainloop()
