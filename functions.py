import os
import string
from math import *

lnames = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel",
          "Mitterand": "François", "Sarkozy": "Nicolas"}

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
                files_names.append(filename)
    return files_names

def names_extract_titles(file):
    file = file[11:][:-4]
    if 48 <= ord(file[-1]) <= 57:
        file = file[:-1]
    return file

def presidents_first_name(lname):
    global lnames
    for k, v in lnames.items():
        if k == lname:
            return v + " " + k
    return None

def display_names_list():
    L = []
    global lnames
    for k, v in lnames.items():
        L.append(v + " " + k)
    return L

def clean_files_lower_case():
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    for i in files_names:
        with open('./speeches/' + i, "r") as f1, open('./cleaned/' + i, "w") as f2:
            for l in f1.readlines():
                for c in l:
                    if 65 <= ord(c) <= 90:
                        c = chr(ord(c)+32)
                    f2.write(c)

def clean_files_punctuation():
    dicoclean = {"e": ["Ã©", "Ã¨", "Ãª"], "c": ["Ã§"], "a": ["Ã", "a¢"], "u": ["a¹", "a»"],
                 "i": ["a®"], " ": list("-'"), "": list("!$%&(),./:;<=>?[]^_`{|}~")}
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    for i in files_names:
        with open('./cleaned/' + i, "r") as f:
            content = f.read()
            for k, v in dicoclean.items():
                for j in v:
                    content = content.replace(j, k)
        with open('./cleaned/' + i, "w", encoding="utf-8") as f:
            f.write(content)

#TF (Term Frequency)
def tf(str):
    L = str.split(' ')
    dico = {}
    for i in range(0,len(L)):
        if L[i] in dico :
            dico[L[i]] += 1
        else:
            dico[L[i]] = 1
    return dico

def idf(directory = "./cleaned"):
    fd = {}
    files_names = list_of_files(directory, "txt")
    for i in files_names:
        with open(directory + "/" + i, "r") as f:
            content = f.readlines()
            for l in content:
                d = tf(l[:-1])
                for k, v in d.items():
                    if k not in fd.keys():
                        fd[k] = 1
                    else:
                        fd[k] += 1
    for k, v in fd.items():
        fd[k] = log(1/v)
    return fd


def transpose_matrix(matrix):
    nbRow = len(matrix)
    nbCol = len(matrix[0])
    transposed_matrix = []
    for j in range(nbCol):
        M = []
        for i in range(nbRow):
            M.append(matrix[i][j])
        transposed_matrix.append(M)
    return transposed_matrix

def tf_idf(directory="./cleaned"):
    tf_idf_matrix = []                                      #init of tf_idf_matrix
    didf = idf()                                            #init of the dict with idf value for all the words
    files_names = list_of_files(directory, "txt")
    for i in files_names:
        fl = ""
        with open(directory + "/" + i, "r") as f:           #for each files we do a calculation of tf*idf to do the matrix
            tf_idf_doc = []
            ls = f.readlines()
            for l in ls:
                fl += l[:-1] + " "
            dtf = tf(fl)                                    #tf score for one document
        for k, v in didf.items():                           #part of code for create the matrix with all the words
            if k not in dtf.keys():
                dtf[k] = 0
            tf_idf_doc.append(dtf[k]*didf[k])
        tf_idf_matrix.append(tf_idf_doc)
    return transpose_matrix(tf_idf_matrix)                                    #we have to transpose the result !!!


def tf_idf_dico(matrix_tfidf, directory="./cleaned"):
    tfidfdico = {"files" : list_of_files(directory, "txt")}
    i = 0
    for k in idf(directory).keys():
        tfidfdico[k] = matrix_tfidf[i]
        i += 1
    return tfidfdico

