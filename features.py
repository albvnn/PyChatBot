from functions import *

def important_words(dico_tfidf):           #feature 1
    L = []
    del dico_tfidf["files"]
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) > 0:
            L.append(k)
    return L

def most_important_word(dico_tfidf):        #feature 2
    del dico_tfidf["files"]
    maxk = ""
    maxv = 0
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) > maxv:
            maxk = k
            maxv = sum(v)/len(v)
    return maxk, maxv

def most_word_of_chirac(dico_tfidf):        #feature 3
    del dico_tfidf["files"]
    mink = ""
    minv = 1000
    for k, v in dico_tfidf.items():
        if minv > v[0] + v[1] / 2:
            mink = k
            minv = v[0] + v[1] / 2
    return mink

def nations_word_on_speeches(dico_tfidf):       #feature 4
    L = []
    del dico_tfidf["files"]
    minname = ""
    minv = 0
    for k, v in dico_tfidf.items():
        for i in range(len(v)):
                if k == "nation" and v[i] != 0:
                    if names_extract_titles(dico_tfidf["files"][i]) not in L:
                        L.append(names_extract_titles(dico_tfidf["files"][i]))
                if v[i] > minv:
                    minname = dico_tfidf["files"][i]
                    minv = v[i]
    return L, names_extract_titles(minname)

def first_pres_to_talk_eco(dico_tfidf):         #feature 5
    minname = ""
    minv = 0
    del dico_tfidf["files"]
    for k, v in dico_tfidf.items():
        for i in range(len(v)):
            if type(v[i]) is int or type(v[i]) is float:
                if k == "climat" or k == "ecologie":
                    if v[i] > minv:
                        minname = names_extract_titles(dico_tfidf["files"][i])
                        minv = v[i]
    return minname

def all_pres_say_words(dico_tfidf):         #feature 6
    L=[]
    status=True
    del dico_tfidf["files"]
    for k, v in dico_tfidf.items():
        for i in v:
            if i == 0:
                status=False
        if status:
            L.append(k)
    return L