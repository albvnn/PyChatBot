from functions import *
from features import *
from tkinter import *
import time

def printSomething(string):
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(win, text= str(string))
    #this creates a new label to the GUI
    label.pack()

def dis_gui():
    win = Tk()
    win.title('chatbot !')
    win.geometry('500x500')

    btn = Button(win, text='Click me !', command=important_words(tf_idf_dico(tf_idf())))
    btn2 = Button(win, text='Click me ! 2', command=win.destroy)
    btn3 = Button(win, text='Click me !', command=win.destroy)
    btn4 = Button(win, text='Click me ! 2', command=win.destroy)
    btn5 = Button(win, text='Click me !', command=win.destroy)
    btn6 = Button(win, text='Click me ! 2', command=win.destroy)
    btn.pack(ipadx=5, ipady=5, expand=True)
    btn2.pack(ipadx=5, ipady=5, expand=True)
    btn3.pack(ipadx=5, ipady=5, expand=True)
    btn4.pack(ipadx=5, ipady=5, expand=True)
    btn5.pack(ipadx=5, ipady=5, expand=True)
    btn6.pack(ipadx=5, ipady=5, expand=True)

    win.mainloop()
