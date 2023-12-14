import os
import string
from clean_functions import clean_lower_case, clean_punctuation
from math import *

lnames = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel",
          "Mitterand": "François", "Sarkozy": "Nicolas"}

def list_of_files(directory, extension):
    """Retrieves a list of file names with the specified extension in the given directory."""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
                files_names.append(filename)
    return files_names

def names_extract_titles(file):
    file = file[11:][:-4] # Remove the first 11 characters and the last 4 characters from the file name

    if 48 <= ord(file[-1]) <= 57: # Check if the last character of the file name is a digit
        file = file[:-1] # If true, remove the last character from the file name

    return file


def presidents_first_name(lname):
    for k, v in lnames.items():
        if k == lname: # Check if the current key (last name) matches the provided last name
            return v + " " + k # If there's a match, concatenate the corresponding value (first name) and the last name
    
    return None # If no match is found, return None


def display_names_list():
    '''Return in a list all the names of the Presidents'''
    L = []
    global lnames
    for k, v in lnames.items():
        L.append(v + " " + k)
    return L

#TF (Term Frequency)
def tf(input_str):
    word_list = input_str.split(' ')
    
    word_freq_dict = {}
    
    for word in word_list:
        if word in word_freq_dict: # Check if the word is already in the dictionary
            word_freq_dict[word] += 1 # If yes, increment its frequency
        else:
            word_freq_dict[word] = 1 # If no, add the word to the dictionary with a frequency of 1
    
    return word_freq_dict


def idf(directory):
    doc_freq = {}
    
    files_names = list_of_files(directory, "txt")
    
    for i in files_names:
        with open(directory + i, "r") as f: # Open the cleaned file for reading
            unique_words = []
            
            content = f.readlines() # Read the content of the file line by line
            
            for line in content:
                line_tf = tf(line[:-1]) # Calculate the term frequency for each line
                
                # Add unique words to the list
                for word in line_tf.keys():
                    if word not in unique_words:
                        unique_words.append(word)
            
            # Update document frequency for each unique word
            for unique_word in set(unique_words):
                if unique_word not in doc_freq.keys():
                    doc_freq[unique_word] = 1
                else:
                    doc_freq[unique_word] += 1
    
    # Calculate the inverse document frequency for each word
    for word, freq in doc_freq.items():
        doc_freq[word] = log10(len(files_names) / freq)
    
    return doc_freq


def transpose_matrix(matrix):
    '''Take a matrix and invert the columns with rows'''
    nbRow = len(matrix)
    nbCol = len(matrix[0])
    transposed_matrix = []
    for j in range(nbCol):
        M = []
        for i in range(nbRow):
            M.append(matrix[i][j])
        transposed_matrix.append(M)
    return transposed_matrix


def tf_idf(directory):
    tf_idf_matrix = []

    didf = idf(directory)

    files_names = list_of_files(directory, "txt")

    for i in files_names:
        fl = ""

        with open(directory + i, "r") as f: # Open the cleaned file for reading
            tf_idf_doc = []

            ls = f.readlines() # Read the content of the file line by line

            for l in ls: # Concatenate lines into a single string
                fl += l[:-1] + " "

            dtf = tf(fl) # Calculate the term frequency for the document

            # Calculate the TF-IDF score for each word in the document
            for k, v in didf.items():
                if k not in dtf.keys():
                    dtf[k] = 0
                tf_idf_doc.append(dtf[k] * didf[k])

            tf_idf_matrix.append(tf_idf_doc) # Append the TF-IDF vector to the matrix

    return transpose_matrix(tf_idf_matrix) # Transpose the TF-IDF matrix


def tf_idf_dico(matrix_tfidf, directory):
    tf_idf_dico = {"files": list_of_files(directory, "txt")} # Initialize the TF-IDF dictionary

    i = 0
    
    for k in idf(directory).keys(): # For each word in the IDF dictionary
        tf_idf_dico[k] = matrix_tfidf[i] # Add the word and its corresponding TF-IDF vector to the dictionary
        i += 1

    del tf_idf_dico['']
    return tf_idf_dico


def question_tf_idf(s, dicoform=False):
    '''Determine the tf idf vector (or dictionary) of the question asked by the user.'''
    tfidfd = tf_idf_dico(tf_idf("./cleaned/"), "./cleaned/")    # Calculate TF-IDF dictionary for the entire corpus
    # Initialize variables for TF-IDF vector and dictionary
    tf_idf_v = []
    tf_idf_d = {}

    s = clean_punctuation(clean_lower_case(s))      # Clean and preprocess the input string
    tfd = tf(s)     # Calculate TF (Term Frequency) vector for the input string
    idfd = idf("./cleaned/")    # Calculate IDF (Inverse Document Frequency) for the entire corpus
    q = list(tfd.keys())    # Create a list 'q' containing terms from the TF vector

    for k in tfidfd.keys():     # Ensure that the TF vector includes all terms found in the TF-IDF dictionary
        if k not in q:
            tfd[k] = 0

    for k, v in idfd.items():     # Calculate the final TF-IDF values

        if k not in tfd.keys():
            tf_idf_v.append(-1)
            tf_idf_d[k] = -1
        else:
            tf_idf_v.append(v * tfd[k])
            tf_idf_d[k] = v * tfd[k]

    if dicoform:        # Return either the TF-IDF vector or dictionary based on the 'dicoform' parameter
        return tf_idf_d
    return tf_idf_v


def norm(a):
    '''Calculate the Euclidean norm of a vector'''
    s = 0
    for i in a:
        s += i ** 2
    return sqrt(s)


def cosine_similarity(a, b):
    '''Calculate the cosine similarity between two vectors'''
    scalar_p = 0
    for i in range(len(a)):
        scalar_p += a[i] * b[i]
    return (scalar_p / norm(a) * norm(b))


def most_significant_document(tfidf_question, tfidf_matrix):
    '''Determine the most significant document that can return a logic answer based on similiraty with tf idf vector of the question'''
    lf = list_of_files("./cleaned", "txt")  # Get the list of files in the "./cleaned" directory with a ".txt" extension

    tfidf_matrix = transpose_matrix(tfidf_matrix)    # Transpose the TF-IDF matrix

    # Initialize variables for iteration and tracking the most significant document
    k = 0
    maxk = 0
    max_cosine_similarity = 0

    # Iterate through the columns (documents) of the transposed TF-IDF matrix
    for i in tfidf_matrix:
        # Calculate cosine similarity between the question and the current document
        cosine_similarity_value = cosine_similarity(tfidf_question, i)

        # Update if the current document has a higher cosine similarity
        if max_cosine_similarity <= cosine_similarity_value:
            max_cosine_similarity = cosine_similarity_value
            maxk = k
        k += 1

    # Return the name of the most significant document based on cosine similarity
    return lf[maxk]


def most_important_question_term(s):
    tfidf_question = question_tf_idf(s, True)   # Calculate the TF-IDF dictionary for the input question string 's'

    # Initialize variables for tracking the most important term
    maxk = ""
    maxv = 0.0

    # Iterate through the terms and their corresponding TF-IDF values in the question
    for k, v in tfidf_question.items():
        # Update if the current term has a higher TF-IDF value
        if maxv < v:
            maxv = v
            maxk = k

    # Return the most important term in the question based on TF-IDF value
    return maxk


def auto_response(most_imp_term, most_sin_doc, s):
    # Define response starters based on question types
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr, ",
        "Donne": "Voici, "
    }

    # Initialize response starter
    starter = ""

    # Check if any predefined question starters are present in the TF vector of the question
    for k, v in question_starters.items():
        if k in tf(s):
            starter = v

    # Open the content of the most significant document in the speeches directory
    with open("./speeches/" + most_sin_doc, "r", encoding="utf-8") as f:
        # Read the lines from the file
        content = f.readlines()
        L = []

        # Preprocess each line by removing trailing newline characters
        for l in content:
            content = l[:-1] + " "
            L.append(content)

        # Process to do a list with eaches sentences separate by '.'
        L = " ".join(L)
        L = L.split(".")

        # Iterate through sentences to find the one containing the most important term
        for i in L:
            if most_imp_term in i:
                # Correct the sentence format if it starts with a space
                for j in i:
                    if i[0] == " ":
                        i = i[1:]

                # Modify the sentence based on the response starter (if present)
                if starter != "":
                    i = i[0].lower() + i[1:]
                    return starter + i
                else:
                    return i

        # If the most important term is not found, provide a default response
        most_imp_term = "Désolé... Je ne comprends pas votre question. Il semblerait que le mot le plus important de votre phrase n'est pas dans le document le plus significatif."
        return most_imp_term
