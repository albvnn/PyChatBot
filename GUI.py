from tkinter import *
def get_sending():
    global LabelOnTime
    LabelOnTime = str(RequestLabel.get())
    return str(LabelOnTime)
def printS():
    global LabelOnTime
    get_sending()
    a = dire(LabelOnTime)
    if a == "/clean":
        DisplayLabel.config(state=NORMAL)
        DisplayLabel.delete("1.0", "end")
        DisplayLabel.config(state=DISABLED)
    else:
        DisplayLabel.config(state=NORMAL)
        DisplayLabel.insert(INSERT, "\n\n" + "You : " + LabelOnTime + "\n\n" + "Bobby : " + a + "\n\n")
        DisplayLabel.config(state=DISABLED)
    RequestLabel.delete("0", "end")

def dire(c):
    command = ['/help', '/features', '/feature1', '/feature2', '/feature3', '/feature4', '/feature5', '/feature6',
               '/info', '/exit', '/clean']
    answer = "This command doesn't exist. \n Please do '/help' for have the list of commands."
    if c in command:
        if c == command[0]:
            answer = ("Hey ! There is few command : "
                      "\n - /help : lists of the differents functions"
                      "\n - /info : some info about me ! "
                      "\n - /features : lists of the differents features "
                      "\n - /feature1 : Displays words with a TD-IDF equal to 0"
                      "\n - /feature2 : Identifies and display the most important word in the documents analyzed."
                      "\n - /feature3 : Display the words most often repeated by President Chirac"
                      "\n - /feature4 : Show the presidents who have spoken of the word 'Nation', and indicate the one who said it the most. "
                      "\n - /feature5 : Show the first president to talk about climate ('climat') and ecology ('écologie')."
                      "\n - /feature6 : Quel(s) mot(s) tous les présidents ont-ils mentionné ? (Excluding 'unimportant' words)"
                      "\n - /clean : for clean the previous discussion between you and me ! "
                      "\n - /exit : exit the app ")
        elif c == command[1]:
            answer = "LIST OF FEATURES"
        elif c == command[2]:
            answer = "There is the list of least important words in the corpus of speeches : " + ", ".join(important_words(tf_idf_dico(tf_idf())))
        elif c == command[3]:
            answer = "FEATURES 2"
        elif c == command[4]:
            answer = "FEATURES 3"
        elif c == command[5]:
            answer = "FEATURES 4"
        elif c == command[6]:
            answer = "FEATURES 5"
        elif c == command[7]:
            answer = "FEATURES 6"
        elif c == command[8]:
            answer = "Hello I'm Bobby ! My creators are Alban and Paul !\nTwo genius who made the better chatbot (better than CHAT GPT)"
        elif c == command[9]:
            exit()
        elif c == command[10]:
            answer = "/clean"
    return answer

def dis_gui():
    global RequestLabel
    global DisplayLabel
    global win
    win = Tk()
    win.title('Bobby - The greatest chatbot !')
    win.geometry('900x600')
    win.resizable(width=False, height=False)
    win.configure(background="#404258")

    DisplayFrame = Frame(win)
    DisplayFrame.place(relx=0.1, rely=0.1)
    DisplayLabel = Text(DisplayFrame, height=20, width=63, font="Roboto", bg="#404258", fg="white", bd=0, wrap=WORD)
    DisplayLabel.pack(side = 'left',fill='x')
    scroll = Scrollbar(DisplayFrame, orient='vertical', command=DisplayLabel.yview)
    scroll.pack(expand='yes', fill='y')

    RequestLabel = Entry(win, width=60, font="Roboto", bg="#474E68", fg="white", insertbackground="white", bd=0)
    RequestLabel.place(relx=0.1, rely=0.9)
    ButtonSend = Button(win, text="Send", command=printS, height=1, pady=10, padx=5, width=5, bd=0, bg="#474E68", fg="white")
    ButtonSend.place(relx=0.85, rely=0.9)

    win.bind('<Return>', lambda event: printS())

    win.mainloop()
