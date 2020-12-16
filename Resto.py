import tkinter as tk
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time.time()))

class Resto:
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 30 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier New} 10 Bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        # Food Info


        self.Label1 = tk.Label(master=top, text='Restaurant Management System', background="#091833", font=font11, foreground="#f2A343")
        self.Label1.place(relx= 0.268, rely= 0.02, height=51, width=507)

        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16, fg="white")
        localtime1.place(relx=0.420, rely=0.12)

        # Food label

        self.Label12 = tk.Label(master=top, text='Order Num :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.054, rely=0.25)
        self.Label12 = tk.Label(master=top, text='Fried Potato :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.044, rely=0.32)
        self.Label12 = tk.Label(master=top, text='Chk Burger :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.053, rely=0.4)
        self.Label12 = tk.Label(master=top, text='Big King :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.078, rely=0.48)
        self.Label12 = tk.Label(master=top, text='Chk Royal :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.060, rely=0.56)
        self.Label12 = tk.Label(master=top, text='Veg Salad :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.055, rely=0.64)
        self.Label12 = tk.Label(master=top, text='Drinks :', foreground='#bac8bd', font=font12, background="#091833")
        self.Label12.place(relx=0.093, rely=0.71)

        # Food Entry
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.26)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.34)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.42)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.5)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.58)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.66)
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.18, rely= 0.73)

        # Calculator
        self.entry1 = tk.Entry(master=top, background="#d9d9d9",foreground="#c60000", selectbackground="#f2a343", font=font10)
        self.entry1.place(relx = 0.705, rely= 0.24, height=35,relwidth= 0.267)
        
        self.Button1 = tk.Button(master=top, text= '''7''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''8''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''9''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''/''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)
       
        self.Button1 = tk.Button(master=top, text= '''1''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''2''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''3''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''-''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text= '''4''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''5''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''6''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text= '''*''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)

        self.Button1 = tk.Button(master=top, text= '''0''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.64, height=35, width=146)
        self.Button1 = tk.Button(master=top, text= '''.''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.64, height=35, width=67)
        self.Button1 = tk.Button(master=top, text= '''+''', background='#122c63', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.64, height=35, width=37)

        self.Button1 = tk.Button(master=top, text= '''=''', background='#f2a343', font=font14, foreground='#ffffff', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.72, height=34, width=272)
        
        
        
root = tk.Tk()
my_gui = Resto(root)
root.mainloop()



