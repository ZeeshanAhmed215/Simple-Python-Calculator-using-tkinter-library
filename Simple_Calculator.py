from tkinter import *
import math

Window=Tk()
Window.geometry("1500x1500")
Window.title("Simple Calculator(➕➖➗)")
Window.minsize(500,650)
Window.maxsize(500,650)
# Functions for performing operations==========================
def Operation():
    try:
        if Sc_value.get()=="":
            Sc_value.set("Error...")
        else:
            data=Sc_value.get()
            final=eval(data)
            Sc_value.set(final)
            Screen.update()
    except (SyntaxError,ZeroDivisionError,KeyError,ValueError):
        Sc_value.set("Error...")

def Square():
    try:
        
        string=Sc_value.get()
        
        if  string=="":
            Sc_value.set("Error...")
            Screen.update()
        else:
            string2=eval(string)
            sq=float(string2)*float(string2)
            Sc_value.set(sq)
            Screen.update()
    except (ValueError,SyntaxError,KeyError):
        Sc_value.set("Error...")
        Screen.update()



def squ_root():
    try:
        
        string=Sc_value.get()
        
        if  string=="":
            Sc_value.set("Error...")
            Screen.update()
        else:
            string2=eval(string)
            sq=math.sqrt(float(string2))
            Sc_value.set(sq)
            Screen.update()        
    except (SyntaxError,ValueError,KeyError):
        Sc_value.set("Error...")
        Screen.update()

def C():
    Sc_value.set("") 
    
def B1():
    Di_old=Sc_value.get()
    Di_new=Di_old+"1"
    Sc_value.set(Di_new)

def B2():
    Di_old=Sc_value.get()
    Di_new=Di_old+"2"
    Sc_value.set(Di_new)

def B3():
    Di_old=Sc_value.get()
    Di_new=Di_old+"3"
    Sc_value.set(Di_new)

def B4():
    Di_old=Sc_value.get()
    Di_new=Di_old+"4"
    Sc_value.set(Di_new)

def B5():
    Di_old=Sc_value.get()
    Di_new=Di_old+"5"
    Sc_value.set(Di_new)

def B6():
    Di_old=Sc_value.get()
    Di_new=Di_old+"6"
    Sc_value.set(Di_new)


def B7():
    Di_old=Sc_value.get()
    Di_new=Di_old+"7"
    Sc_value.set(Di_new)

def B8():
    Di_old=Sc_value.get()
    Di_new=Di_old+"8"
    Sc_value.set(Di_new)

def B9():
    Di_old=Sc_value.get()
    Di_new=Di_old+"9"
    Sc_value.set(Di_new)

def B0():
    Di_old=Sc_value.get()
    Di_new=Di_old+"0"
    Sc_value.set(Di_new) 

def B00():
    Di_old=Sc_value.get()
    Di_new=Di_old+"00"
    Sc_value.set(Di_new)
def Bplus():
    Di_old=Sc_value.get()
    Di_new=Di_old+"+"
    Sc_value.set(Di_new)
def Bminus():
    Di_old=Sc_value.get()
    Di_new=Di_old+"-"
    Sc_value.set(Di_new)
def Bmulti():
    Di_old=Sc_value.get()
    Di_new=Di_old+"*"
    Sc_value.set(Di_new)
def Bdivide():
    Di_old=Sc_value.get()
    Di_new=Di_old+"/"
    Sc_value.set(Di_new)
def Bdot():
    Di_old=Sc_value.get()
    Di_new=Di_old+"."
    Sc_value.set(Di_new)

def Bcross():
    Di_old=Sc_value.get()
    Di_new=Di_old[0:len(Di_old)-1]
    Sc_value.set(Di_new)
    Screen.update()
# Variables for buttons========================================

Sc_value=StringVar()
Sc_value.set("")

Screen=Entry(Window, width=24, textvariable=Sc_value, font=("Times 30 bold"),bd=1,relief=SOLID)
Screen.pack()
Big_fram = Frame(Window, bg="#ffffff", padx=10, pady=10, bd=3, relief=RIDGE)
Big_fram.pack( padx=10, pady=10, fill=BOTH ,expand=True)


# First Row===============================================================
Bt1=Button(Big_fram, text="1",relief=RAISED,bd=7,command=B1,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=0, column=0,pady=10,padx=10 )
Bt2=Button(Big_fram, text="2",relief=RAISED,bd=7,command=B2,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=0, column=1,pady=10,padx=20 )
BtC=Button(Big_fram, text="C",relief=RAISED,bd=7,command=C,
        bg="#FF1A1A", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=0, column=2,pady=10,padx=10 )

# Second Row===============================================================
Bt3=Button(Big_fram, text="3",relief=RAISED,bd=7,command=B3,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=1, column=0,pady=10,padx=10 )
Bt4=Button(Big_fram, text="4",relief=RAISED,bd=7,command=B4,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=1, column=1,pady=10,padx=20 )
Bt_cross=Button(Big_fram, text="❌",relief=RAISED,bd=7,command=Bcross,
        bg="#FF1A1A", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=1, column=2,pady=10,padx=10 )

# Third Row===============================================================
Bt5=Button(Big_fram, text="5",relief=RAISED,bd=7,command=B5,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=2, column=0,pady=10,padx=10 )
Bt6=Button(Big_fram, text="6",relief=RAISED,bd=7,command=B6,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=2, column=1,pady=10,padx=20 )
Bt_plus=Button(Big_fram, text="➕",relief=RAISED,bd=7,command=Bplus,
        bg="#1e9600", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=2, column=2,pady=10,padx=10 )

# Fourth Row===============================================================
Bt7=Button(Big_fram, text="7",relief=RAISED,bd=7,command=B7,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=3, column=0,pady=10,padx=10 )
Bt8=Button(Big_fram, text="8",relief=RAISED,bd=7,command=B8,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=3, column=1,pady=10,padx=20 )
Bt_minus=Button(Big_fram, text="➖",relief=RAISED,bd=7,command=Bminus,
        bg="#1e9600", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=3, column=2,pady=10,padx=10 )

# Fifth Row===============================================================
Bt9=Button(Big_fram, text="9",relief=RAISED,bd=7,command=B9,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=4, column=0,pady=10,padx=10 )
Bt0=Button(Big_fram, text="0",relief=RAISED,bd=7,command=B0,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=4, column=1,pady=10,padx=20 )
Bt_multi=Button(Big_fram, text="❌",relief=RAISED,bd=7,command=Bmulti,
        bg="#1e9600", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=4, column=2,pady=10,padx=10 )

# Sixth Row===============================================================
Bt_sqrt=Button(Big_fram, text="x½",relief=RAISED,bd=7,command=squ_root,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=5, column=0,pady=10,padx=10 )
Bt_expon=Button(Big_fram, text="x²",relief=RAISED,bd=7, 
        bg="#424444", fg="white", font=("lucida", 17, "bold"),command=Square,
        width=7).grid(row=5, column=1,pady=10,padx=20 )
Bt_divide=Button(Big_fram, text="➗",relief=RAISED,bd=7,command=Bdivide,
        bg="#1e9600", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=5, column=2,pady=10,padx=10 )


Bt00=Button(Big_fram, text="00",relief=RAISED,bd=7,command=B00,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=6, column=0,pady=10,padx=10 )
Bt_equal=Button(Big_fram, text="✔️",relief=RAISED,bd=7, command=Operation,
        bg="#424444", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=6, column=1,pady=10,padx=20 )
Bt_dot=Button(Big_fram, text="⚫",relief=RAISED,bd=7,command=Bdot,
        bg="#1e9600", fg="white", font=("lucida", 17, "bold"),
        width=7).grid(row=6, column=2,pady=10,padx=10 )
Window.mainloop()

