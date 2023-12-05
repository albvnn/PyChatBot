import os
if not os.path.isdir("cleaned"):
    os.mkdir(os.path.join(os.getcwd(), "cleaned"))
from clean_functions import *

clean_files_lower_case()
clean_files_punctuation()

from GUI import *

if __name__ == "__main__":
    #print(idf("./cleaned/"))
    a = question_tf_idf("Donne donne climat donne moi des réponses ?")
    b = tf_idf("./cleaned/")
    y = most_significant_document(a, b)
    z = most_important_question_term("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")
    print(auto_response(z, y))
