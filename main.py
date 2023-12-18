import os
if not os.path.isdir("cleaned"):
    os.mkdir(os.path.join(os.getcwd(), "cleaned"))
from clean_functions import *

clean_files_lower_case()
clean_files_punctuation()

from GUI import *

if __name__ == "__main__":
    dis_gui()
