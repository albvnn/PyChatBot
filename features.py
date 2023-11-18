from functions import *

def important_words(dico_tfidf):           #feature 1
    L = []
    dico_tfidf["files"] = [0]*8
    for k, v in dico_tfidf.items():
        if -50 < sum(v)/len(v) < 0:
            L.append(k)
    return L

def most_important_word(dico_tfidf):        #feature 2
    dico_tfidf["files"] = [0]*8
    maxk = ""
    maxv = -1000
    for k, v in dico_tfidf.items():
        if maxv <= sum(v)/len(v) < 0:
            maxk = k
            maxv = sum(v)/len(v)
    return maxk

def most_word_of_chirac(dico_tfidf):        #feature 3
    dico_tfidf["files"] = [0]*8
    mink = ""
    minv = -0.1
    for k, v in dico_tfidf.items():
        if v[0] + v[1] / 2 < minv:
            mink = k
            minv = v[0] + v[1] / 2
    return mink

def nations_word_on_speeches(dico_tfidf):       #feature 4
    L = []
    minname = ""
    minv = -0.1
    for k, v in dico_tfidf.items():
            for i in range(len(v)):
                if type(v[i]) is int or type(v[i]) is float:
                    if k == "nation" and v[i] != 0:
                        if names_extract_titles(dico_tfidf["files"][i]) not in L:
                            L.append(names_extract_titles(dico_tfidf["files"][i]))
                    if v[i] < minv:
                        minname = dico_tfidf["files"][i]
                        minv = v[i]
    return L, names_extract_titles(minname)

def first_pres_to_talk_eco(dico_tfidf):         #feature 5
    minname = ""
    minv = -0.1
    for k, v in dico_tfidf.items():
        for i in range(len(v)):
            if type(v[i]) is int or type(v[i]) is float:
                if k == "climat" or k == "ecologie":
                    if v[i] < minv:
                        minname = names_extract_titles(dico_tfidf["files"][i])
                        minv = v[i]
    return minname

def all_pres_say_words(dico_tfidf):         #feature 6
    L=[]
    for k, v in dico_tfidf.items():
        if type(v[1]) is int or type(v[1]) is float:
            if 0 not in v:
                L.append(k)
    return L