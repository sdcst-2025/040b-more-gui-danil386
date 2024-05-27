import tkinter as t


w = t.Tk()
w.geometry("650x600")
w.attributes('-topmost',True)

ig = [
    t.PhotoImage(file="main.png"),
    t.PhotoImage(file="minimap.png"),
    t.PhotoImage(file="logo.png")
    
]
l = {
    "main" : t.Label(w,image=ig[0]),
    "mini" : t.Label(w,image=ig[1]),
    "logo" : t.Label(w,image=ig[2])
    
}
b = {
    "w" : t.Button(w,text="W",anchor="center"),
    "e" : t.Button(w,text="E",anchor="center"),
    "s" : t.Button(w,text="S",anchor="center"),
    "n" : t.Button(w,text="N",anchor="center"),
    "sw" : t.Button(w,text="SW",anchor="center"),
    "nw" : t.Button(w,text="NW",anchor="center"),
    "ne" : t.Button(w,text="NE",anchor="center"),
    "se" : t.Button(w,text="SE",anchor="center")    
}

rb = [
    t.Button(w,text="MAP", anchor="center"),
    t.Button(w,text="INVENTORY", anchor="center"),
    t.Button(w,text="POKEDEX", anchor="center"),
    t.Button(w,text="ROSTER", anchor="center"),
    t.Button(w,text="JOURNAL", anchor="center"),
    t.Button(w,text="HELP", anchor="center"),
    t.Button(w,text="SHOP", anchor="center")
    
]
cy =490
t.Label(w,text="POKEMON ADVENTURE",anchor="center").place(x=30,y=5,height=30,width=590)
t.Label(w,text="MINI MAP",anchor="center").place(x=520,y=60,height=30,width=100)

b['nw'].place(x=10,y=cy,width=30,height=30)
b['n'].place(x=40,y=cy,width=30,height=30)
b['ne'].place(x=70,y=cy,width=30,height=30)
b['w'].place(x=10,y=cy+30,width=30,height=30)
b['e'].place(x=70,y=cy+30,width=30,height=30)
b['sw'].place(x=10,y=cy+60,width=30,height=30)
b['s'].place(x=40,y=cy+60,width=30,height=30)
b['se'].place(x=70,y=cy+60,width=30,height=30)


for i in range(0,len(rb)):
    rb[i].place(x= 520,y=190+i*40,height=40,width=100)
    pass
l["main"].place(x=10,y=40)
l["mini"].place(x=520,y=90)
l["logo"].place(x=270,y=510)

w.mainloop()