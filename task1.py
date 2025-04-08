import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("385x85")
window.attributes("-topmost", True)
window.resizable(False,False)

nF = Frame()
nF1 = Frame(nF)
nF2 = Frame(nF)
nF3 = Frame(nF)
nF5 = Frame()


flabel1 = tk.Label(nF1,text="Principal")
fentry1 = tk.Entry(nF1,text="Entry widgets can be typed in", width=22)
flabel2 = tk.Label(nF2,text="Interest Rate")
fentry2 = tk.Entry(nF2,text="Entry widgets can be typed in", width=22)
flabel3 = tk.Label(nF3,text="Years")
combo = ttk.Combobox(nF3,values=["1","2","3","4","5","6","7","8","9","10"])
flabel4 = tk.Label(window, text = "-")
flabel5 = tk.Label(nF5,text="Amount")
fentry5 = tk.Entry(nF5,text="Entry widgets can be typed in", width=22)


nF.pack(pady=0)
nF1.pack(side = LEFT)
flabel1.pack()
fentry1.pack()

nF2.pack(side = LEFT)
flabel2.pack()
fentry2.pack()

nF3.pack(side = LEFT)
flabel3.pack()
combo.pack()

flabel4.pack(padx=(0,250))

nF5.pack(padx=(0,28))
flabel5.pack(side = LEFT)
fentry5.pack(side = LEFT)

window.mainloop()