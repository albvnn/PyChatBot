from functions import *
from features import *
from GUI import *

if __name__ == "__main__":
    clean_files_lower_case()
    clean_files_punctuation()
    print(all_pres_say_words(tf_idf_dico(tf_idf())))
