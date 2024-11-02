from tkinter import *
import tkinter as tk
window = Tk()
window.title("calculator")
window.configure(bg="white")
#window.geometry("400x500")

T=Text(window,width=7,height=5)
#T.pack()
T.insert(tk.END,"")

def append_value(value):
    T.insert(tk.END, value)  # Append the value to the text box

def clr_value():
    T.delete("1.0","end")

def delete_last():
    T.delete("end-2c", "end-1c") 

B1 = Button(window, text ="1",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("1"))
B2 = Button(window, text ="2",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("2"))
B3 = Button(window, text ="3",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("3"))
B4 = Button(window, text ="4",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("4"))
B5 = Button(window, text ="5",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("5"))
B6 = Button(window, text ="6",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("6"))
B7 = Button(window, text ="7",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("7"))
B8 = Button(window, text ="8",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("8"))
B9 = Button(window, text ="9",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("9"))
B0 = Button(window, text ="0",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("0"))
BANS = Button(window, text ="=",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=clr_value)
BAC = Button(window, text ="AC",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=clr_value)
BPLUS = Button(window, text ="+",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("+"))
BMINUS = Button(window, text ="-",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("-"))
BMUL = Button(window, text ="*",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("x"))
BDIV = Button(window, text ="/",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("/"))
BMOD = Button(window, text ="%",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda: append_value("%"))
BDEL = Button(window, text ="DEL",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=delete_last)
BLB = Button(window, text ="(",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda:append_value("("))
BRB = Button(window, text =")",width=7,height=3,bg="#415081",fg="white",font=('Times New Roman',10, 'bold'),command=lambda:append_value(")"))


B7.grid(row=2,column=0)
B8.grid(row=2,column=1)
B9.grid(row=2,column=2)
B4.grid(row=3,column=0)
B5.grid(row=3,column=1)
B6.grid(row=3,column=2)
B1.grid(row=4,column=0)
B2.grid(row=4,column=1)
B3.grid(row=4,column=2)
B0.grid(row=5,column=0)
BAC.grid(row=1,column=0)
BDEL.grid(row=1,column=1)
BMOD.grid(row=1,column=2)
BDIV.grid(row=1,column=3)
BMUL.grid(row=2,column=3)
BMINUS.grid(row=3,column=3)
BPLUS.grid(row=4,column=3)
BANS.grid(row=5,column=3)
BLB.grid(row=5,column=1)
BRB.grid(row=5,column=2)

T.grid(row=0,column=0)

window.mainloop()



print("done")

