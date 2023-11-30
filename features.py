from functions import *

def unimportant_words(dico_tfidf):           #feature 1
    '''Identifies words that have a TF-IDF score of 0 across all documents in the corpus.'''
    L = []
    del dico_tfidf["files"]
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) == 0.0:
            L.append(k)
    return L

unimportant_words = unimportant_words(tf_idf_dico(tf_idf("./cleaned/"), "./cleaned/"))
def most_important_word(dico_tfidf):        #feature 2
    '''This function finds the word with the highest average TF-IDF score across all documents.'''
    del dico_tfidf["files"]
    maxk = ""
    maxv = 0
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) > maxv:
            maxk = k
            maxv = sum(v)/len(v)
    return maxk

def most_word_of_chirac():        #feature 3
    '''Reads two files related to Chirac's nominations, combines the text, calculates the term frequency, and returns the word with the highest frequency.'''
    fl = ""
    with open('./cleaned/Nomination_Chirac1.txt', 'r') as f1, open('./cleaned/Nomination_Chirac2.txt', 'r') as f2:
        ls = f1.readlines()
        ls2 = f2.readlines()
        for l in ls:
            fl += l[:-1] + " "
        for k in ls2:
            fl += k[:-1] + " "
        fl = tf(fl)
    maxiv = 0
    maxik = ""
    for k, v in fl.items():
        if v >= maxiv:
            maxiv = v
            maxik = k
    return maxik, maxiv

def nations_word_on_speeches(dico_tfidf):       #feature 4
    '''This function looks for documents where the word "nation" has a non-zero TF-IDF score and returns a list of titles and the title with the minimum TF-IDF score.'''
    L = []
    minname = ""
    minv = 0
    for k, v in dico_tfidf.items():
        for i in range(len(v)):
            if type(v[i]) is int or type(v[i]) is float:
                if k == "nation" and v[i] != 0:
                    if names_extract_titles(dico_tfidf["files"][i]) not in L:
                        L.append(names_extract_titles(dico_tfidf["files"][i]))
                if v[i] > minv:
                    minname = dico_tfidf["files"][i]
                    minv = v[i]
    return L, names_extract_titles(minname)

def first_pres_to_talk_eco(dico_tfidf):         #feature 5
    '''Identifies the president who first talked about "climat" or "ecologie" based on the highest TF-IDF score.'''
    minname = ""
    minv = 0
    for k, v in dico_tfidf.items():
        for i in range(len(v)):
            if type(v[i]) is int or type(v[i]) is float:
                if k == "climat" or k == "ecologie":
                    if v[i] > minv:
                        minname = names_extract_titles(dico_tfidf["files"][i])
                        minv = v[i]
    return minname


def all_pres_say_words(dico_tfidf):         #feature 6
    '''F6'''
    global unimportant_words
    del dico_tfidf["files"]
    L = []
    for k,v in dico_tfidf.items():
        if k not in unimportant_words:
            if v[0] + v[1] != 0 and v[5] + v[6] != 0:
                v = list(set(v) - {v[0], v[1], v[5], v[6]})
                if 0.0 not in v:
                    L.append(k)
    return L