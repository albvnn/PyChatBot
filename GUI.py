from command_GUI import *
from tkinter import *
import time

def get_sending():
    global LabelOnTime
    LabelOnTime = str(RequestLabel.get())
    return str(LabelOnTime)
def printS():
    global LabelOnTime
    get_sending()
    a = dire(LabelOnTime)
    DisplayLabel.config(text=a)

def dis_gui():
    global RequestLabel
    global DisplayLabel
    win = Tk()
    win.title('Bobby - The greatest chatbot !')
    win.geometry('900x600')
    win.resizable(width=False, height=False)
    win.configure(background="#404258")

    DisplayLabel = Label(win, height=20, width=63, font="Roboto", bg="#404258", fg="white", bd=0, anchor="nw", wraplength=650, justify="left")
    DisplayLabel.place(relx=0.1, rely=0.1)
    RequestLabel = Entry(win, width=60, font="Roboto", bg="#474E68", fg="white", insertbackground="white", bd=0)
    RequestLabel.place(relx=0.1, rely=0.9)
    ButtonSend = Button(win, text="Send", command=printS, height=1, pady=10, padx=5, width=5, bd=0, bg="#474E68", fg="white")
    ButtonSend.place(relx=0.85, rely=0.9)

    #Button(win, text="Disable", fg="white", bg="black", width=20).pack(pady=20)

    win.mainloop()
