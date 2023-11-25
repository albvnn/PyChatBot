import os
from functions import list_of_files

def clean_files_lower_case():
    directory = "./speeches"  # Specify the directory containing the original speeches

    files_names = list_of_files(directory, "txt")  # Get the list of file names with the extension '.txt'

    for i in files_names:
        with open('./speeches/' + i, "r") as f1, open('./cleaned/' + i,
                                                      "w") as f2:  # Open the original file for reading and the cleaned for writing
            for l in f1.readlines():
                for c in l:
                    if 65 <= ord(c) <= 90:  # Check if the character is an uppercase letter
                        c = chr(ord(c) + 32)  # Convert the uppercase letter to lowercase
                    f2.write(c)  # Write the character to the cleaned file


def clean_files_punctuation():
    dicoclean = {"e": ["Ã©", "Ã¨", "Ãª", "a‰"], "c": ["Ã§"], "a": ["Ã", "a¢", "a€", "Ã%"], "u": ["a¹", "a»"],
                 "i": ["a®", "a¯"], "o": ["a´"], "oe": ["Âœ"], " ": ["-", "'", " "], "": list(
            '"!$%&(),./:;<=>?[]^_`{|}~')}  # Define a dictionary to map replacements for specific characters

    directory = "./cleaned"

    files_names = list_of_files(directory, "txt")  # Get the list of file names with the "txt" extension

    for i in files_names:
        with open('./cleaned/' + i, "r") as f:  # Open the cleaned file for reading
            content = f.read()  # Read the content of the file

            for k, v in dicoclean.items():  # Iterate through the dictionary and replace specific character sequences
                for j in v:
                    content = content.replace(j, k)

        with open('./cleaned/' + i, "w", encoding="utf-8") as f:  # Write the modified content back to the cleaned file
            f.write(content)


def clean_all_files():
    if not os.path.isdir("cleaned"):
        os.mkdir(os.path.join(os.getcwd(), "cleaned"))
        clean_files_lower_case()
        clean_files_punctuation()
    return "./cleaned/"