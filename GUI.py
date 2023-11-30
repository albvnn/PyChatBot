'''Import libraries'''
from tkinter import *
from tkinter import ttk
from features import *
from functions import *
from clean_functions import *

d = clean_all_files()
def get_sending():
    '''Assigns the string representation of the variable 'requestlabel' and 'LabelOnTime' and returns this value as a string.'''
    global LabelOnTime
    LabelOnTime = str(requestlabel.get())
    return str(LabelOnTime)
def printS():
    '''Updates the displaylabel, clearing the input field if the response is "/clean."'''
    global LabelOnTime
    get_sending()
    a = dire(LabelOnTime)
    if a == "/clean":
        displaylabel.config(state=NORMAL)
        displaylabel.delete("1.0", "end")
        displaylabel.config(state=DISABLED)
    else:
        displaylabel.config(state=NORMAL)
        displaylabel.insert(INSERT, "\n\n" + "You : " + LabelOnTime + "\n\n" + "Bobby : " + a + "\n\n")
        displaylabel.config(state=DISABLED)
    requestlabel.delete("0", "end")

def dire(c):
    '''Handles commands and provides corresponding responses, including information about available features, commands, and specific functionalities.'''
    command = [['/help'], ['/features', '/f'], ['/feature1', '/f1'], ['/feature2', '/f2'], ['/feature3', '/f3'], ['/feature4', '/f4'], ['/feature5', '/f5']
        , ['/feature6', '/f6'], ['/info'], ['/exit'], ['/clean']]
    answer = "This command doesn't exist. \n Please do '/help' for have the list of commands."
    if c in command[0]:
        answer = ("Hey ! There is few command : "
                  "\n - '/help' : lists of the differents functions"
                  "\n - '/info' : some info about me ! "
                  "\n - '/features' or '/f' : lists of the differents features "
                  "\n - '/clean' : for clean the previous discussion between you and me ! "
                  "\n - '/exit' : exit the app ")
    elif c in command[1]:
        answer = ("There is few features :"
                  "\n - '/feature1' or '/f1' : Displays words with a TD-IDF equal to 0, so the unimportant words."
                  "\n - '/feature2' or '/f2' : Identifies and display the most important word in the documents analyzed."
                  "\n - '/feature3' or '/f3' : Display the words most often repeated by President Chirac."
                  "\n - '/feature4' or '/f4' : Show the presidents who have spoken of the word 'Nation', and indicate the one who said it the most. "
                  "\n - '/feature5' or '/f5' : Show the first president to talk about climate ('climat') and ecology ('écologie')."
                  "\n - '/feature6' or '/f6' : What word(s) did all the presidents mention? (Excluding 'unimportant' words)")
    elif c in command[2]:
        answer = "There is the least important words in the corpus of speeches : " + ", ".join(unimportant_words(tf_idf_dico(tf_idf(d), d)))
    elif c in command[3]:
        answer = "The word with the maximum TF-IDF is '" + most_important_word(tf_idf_dico(tf_idf(d),d)) + "'"
    elif c in command[4]:
        t = most_word_of_chirac()
        answer = ("'" + t[0] + "' is the most repeted word by Jacques Chirac.\n"
                               "For information this word has been repeted "+
                  str(t[1]) + " times !")
    elif c in command[5]:
        t = nations_word_on_speeches(tf_idf_dico(tf_idf(d), d))
        answer = ("Presidents who have speak about Nation are " + ", ".join(t[0]) +
                  " and the one who repeted the most is " + presidents_first_name(t[1]))
    elif c in command[6]:
        answer = "The first president who talked about ecology or climat is " + presidents_first_name(first_pres_to_talk_eco(tf_idf_dico(tf_idf(d),d)))
    elif c in command[7]:
        answer = ("All the presidents say this words : " + ", ".join(all_pres_say_words(tf_idf_dico(tf_idf(d), d))))
    elif c in command[8]:
        answer = "Hello I'm Bobby ! My creators are Alban and Paul !\nTwo genius who made the best chatbot (better than CHAT GPT)"
    elif c in command[9]:
        exit()
    elif c in command[10]:
        answer = "/clean"
    return answer

def dis_gui():
    '''Sets up the graphical user interface for the chatbot.'''
    global requestlabel
    global displaylabel
    global win
    win = Tk()
    win.title('Bobby - The greatest chatbot !')
    win.geometry('900x600')
    win.resizable(width=False, height=False)
    win.configure(background="#404258")

    displayframe = Frame(win)
    displayframe.place(relx=0.1, rely=0.1)
    welcomelabel = Label(win, text="Bobby Chatbot Interface", bg="#404258", fg="white", bd=0, font=("Roboto", 25, "bold"))
    welcomelabel.place(relx=0.1, rely=0.05)
    scroll = ttk.Scrollbar(displayframe, orient='vertical')
    scroll.pack(expand=1, fill='y', side='right')
    displaylabel = Text(displayframe, height=20, width=63, font="Roboto", bg="#404258", fg="white", bd=0, wrap=WORD,
                        yscrollcommand=scroll.set, selectbackground="black")
    displaylabel.pack(side = 'left',fill='x')


    requestlabel = Entry(win, width=60, font="Roboto", bg="#474E68", fg="white", insertbackground="white", bd=0,
                         selectbackground="black")
    requestlabel.place(relx=0.1, rely=0.9)
    buttonsend = Button(win, text="Send", command=printS, height=1, pady=10, padx=5, width=5, bd=0, bg="#474E68", fg="white")
    buttonsend.place(relx=0.85, rely=0.9)

    win.bind('<Return>', lambda event: printS())

    win.mainloop()
