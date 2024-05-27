import tkinter as tk
from tkinter import ttk


w = tk.Tk()
w.attributes('-topmost',True)

l = []
l.append(tk.Label(w,text="Principal"))
l.append(tk.Label(w,text="Interest Rate"))
l.append(tk.Label(w,text="Years"))
l.append(tk.Label(w,text="-"))
l.append(tk.Label(w,text="Amount"))

e = [
    tk.Entry(w),
    tk.Entry(w),
    tk.Entry(w),
    tk.Entry(w)
    
]
c = tk.ttk.Combobox(w,values=[1,2,3,4,5])

l[0].grid(row=1,column=1)
l[1].grid(row=1,column=2)
l[2].grid(row=1,column=3)
e[0].grid(row=2,column=1)
e[1].grid(row=2,column=2)
c.grid(row=2,column=3)
l[3].grid(row=3,column=1)
l[4].grid(sticky=tk.E,row=4,column=1,)
e[3].grid(row=4,column=2)
w.mainloop()

