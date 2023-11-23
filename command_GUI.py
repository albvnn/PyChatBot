from functions import *
from features import *

def dire(c):
    command = ['help', 'features', 'feature 1', 'feature 2', 'feature 3', 'feature 4', 'feature 5', 'feature 6', 'info']
    answer = "This command doesn't exist. \n Please do 'help' for have the list of commands."
    if c in command:
        if c == command[0]:
            answer = ("Hey ! There is few command : "
                      "\n - help : lists of the differents functions"
                      "\n - features : lists of the differents features "
                      "\n - feature 1 : f1 "
                      "\n - feature 2 : f2 "
                      "\n - feature 3 : f3 "
                      "\n - feature 4 : f4 "
                      "\n - feature 5 : f5 "
                      "\n - feature 6 : f6 "
                      "\n - info : some info about me ! ")
        elif c == command[1]:
            answer = "LIST OF FEATURES"
        elif c == command[2]:
            answer = "FEATURES 1"
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
            answer = "So... I'm Bobby ! My creators are Alban and Paul !\nTwo genius who make the better chatbot (better than CHAT GPT)"
    return answer

