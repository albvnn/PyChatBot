import os

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

#fix this function
def clean_files_punctuation():
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    for i in files_names:
        with open('./cleaned/' + i, "r") as fr, open('./cleaned/' + i + "temp", "w") as fw:
            for l in fr.readlines():
                for c in l:
                    print(ord(c))
                    if 33 <= ord(c) <= 47 or 58 <= ord(c) <= 64 or 91 <= ord(c) <= 96:
                        if c == " " or c == "-" or c == "'":
                            c = " "
                        else:
                            c = ""
                    fw.write(c)
                    fw.write(c)
        os.remove('./cleaned/' + i)
        os.rename('./cleaned/' + i + "temp", './cleaned/' + i)
