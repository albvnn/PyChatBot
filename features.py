from functions import *

def important_words(dico_tfidf):           #feature 1
    '''Identifies words that have a TF-IDF score of 0 across all documents in the corpus.'''
    L = []
    del dico_tfidf["files"]
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) > 0:
            L.append(k)
    return L

def most_important_word(dico_tfidf):        #feature 2
    '''This function finds the word with the highest average TF-IDF score across all documents.'''
    del dico_tfidf["files"]
    maxk = ""
    maxv = 0
    for k, v in dico_tfidf.items():
        if sum(v)/len(v) > maxv:
            maxk = k
            maxv = sum(v)/len(v)
    return maxk, maxv

def most_word_of_chirac(dico_tfidf):        #feature 3
    '''Reads two files related to Chirac's nominations, combines the text, calculates the term frequency, and returns the word with the highest frequency.'''
    del dico_tfidf["files"]
    mink = ""
    minv = 1000
    for k, v in dico_tfidf.items():
        if minv > v[0] + v[1] / 2 > 0:
            mink = k
            minv = v[0] + v[1] / 2
            print(mink, minv)
    return mink

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
    '''Identifies words that are said by all presidents based on non-zero TF-IDF values across different documents.'''
    L=[]
    status=True
    for k, v in dico_tfidf.items():
        for i in v:
            if i == 0:
                status=False
        if status:
            L.append(k)
    return L