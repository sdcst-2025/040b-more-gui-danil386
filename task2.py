import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("630x550")
window.title("POKEMON ADVENTURE")
window.attributes("-topmost", True)
window.resizable(False,False)

nF1 = Frame()
nF2 = Frame()
nF3 = Frame()
nF4 = Frame()

mainscreen = PhotoImage(file="main.png")
label0 = tk.Label(window, image=mainscreen, borderwidth=0)
label1 = tk.Label(window, text="MINI MAP")
minimap = PhotoImage(file="minimap.png")
label2 = tk.Label(window, image=minimap, borderwidth=0)
logo = PhotoImage(file="logo.png")
label3 = tk.Label(window, image=logo, borderwidth=0)
flabel1 = tk.Button(nF1,text="MAP",width=13,height=2)
flabel2 = tk.Button(nF1,text="INVENTORY",width=13,height=2)
flabel3 = tk.Button(nF1,text="POKEDEX",width=13,height=2)
flabel4 = tk.Button(nF1,text="ROSTER",width=13,height=2)
flabel5 = tk.Button(nF1,text="JOURNAL",width=13,height=2)
flabel6 = tk.Button(nF1,text="HELP",width=13,height=2)
flabel7 = tk.Button(nF1,text="SHOP",width=13,height=2)
f2label1 = tk.Button(nF2,text="NW",width=3,height=1)
f2label2 = tk.Button(nF2,text="N",width=3,height=1)
f2label3 = tk.Button(nF2,text="NE",width=3,height=1)
f3label1 = tk.Button(window,text="W",width=3,height=1)
f3label2 = tk.Button(window,text="E",width=3,height=1)
f4label1 = tk.Button(nF4,text="SW",width=3,height=1)
f4label2 = tk.Button(nF4,text="S",width=3,height=1)
f4label3 = tk.Button(nF4,text="SE",width=3,height=1)


label0.place(x=10,y=0)
label1.place(x=525,y=10)
label2.place(x=510,y=30)

nF1.place(x=510,y=125)
flabel1.pack()
flabel2.pack()
flabel3.pack()
flabel4.pack()
flabel5.pack()
flabel6.pack()
flabel7.pack()

nF2.place(x=10,y=450)
f2label1.pack(side=LEFT)
f2label2.pack(side=LEFT)
f2label3.pack(side=LEFT)

f3label1.place(x=10,y=475)

f3label2.place(x=72,y=475)

nF4.place(x=10,y=500)
f4label1.pack(side=LEFT)
f4label2.pack(side=LEFT)
f4label3.pack(side=LEFT)

label3.place(x=275,y=475)

window.mainloop()