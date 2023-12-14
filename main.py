import os

# Check if a directory named "cleaned" does not exist
if not os.path.isdir("cleaned"):
    # If not, create the "cleaned" directory using the 'os.mkdir' function
    os.mkdir(os.path.join(os.getcwd(), "cleaned"))

from clean_functions import *

# Call the 'clean_files_lower_case' function to perform file content transformation to lowercase
clean_files_lower_case()

# Call the 'clean_files_punctuation' function to remove punctuation from file content
clean_files_punctuation()

from GUI import *

# Check if the script is the main program being executed
if __name__ == "__main__":
    # If true, call the 'dis_gui' function to display the graphical user interface
    dis_gui()
