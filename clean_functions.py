import os
def list_of_files(directory, extension):
    """Retrieves a list of file names with the specified extension in the given directory."""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
                files_names.append(filename)
    return files_names

def clean_lower_case(s):
    for a in s:
        if 65 <= ord(a) <= 90:  # Check if the character is an uppercase letter
            c = chr(ord(a) + 32)    # Convert the uppercase letter to lowercase using ASCII values
            s = s.replace(a, c)    # Replace the original uppercase letter with the lowercase one in the string
    return s

def clean_punctuation(s):
    # Dictionary mapping base characters to their variations (accents, special characters)
    dicoclean = {"e": ["é", "è", "ê", "ë"], "c": ["ç"], "a": ["à", "â", "ä", "Ã%"], "u": ["û", "ü"],
                 "i": ["ï", "î"], "o": ["ô"], "oe": ["œ"], " ": ["-", "'", " "], "": list(
            '"!$%&(),./:;<=>?[]^_`{|}~')}
    # Iterate through the dictionary and replace specified characters in the string
    for k, v in dicoclean.items():
        for j in v:
            s = s.replace(j, k)
    return s


def clean_files_lower_case():
    directory = "./speeches"  # Specify the directory containing the original speeches

    files_names = list_of_files(directory, "txt")  # Get the list of file names with the extension '.txt'

    for i in files_names:
        with open('./speeches/' + i, "r") as f1, open('./cleaned/' + i,
                                                      "w") as f2:  # Open the original file for reading and the cleaned for writing
            for l in f1.readlines():
                f2.write(clean_lower_case(l))  # Write the character to the cleaned file


def clean_files_punctuation():
    dicoclean = {"e": ["é", "è", "ê", "ë"], "c": ["ç"], "a": ["à", "â", "ä", "Ã%"], "u": ["û", "ü"],
                 "i": ["ï", "î"], "o": ["ô"], "oe": ["œ"], " ": ["-", "'", " "], "": list(
            '"!$%&(),./:;<=>?[]^_`{|}~')}

    directory = "./cleaned"

    files_names = list_of_files(directory, "txt")  # Get the list of file names with the "txt" extension

    for i in files_names:
        with open('./cleaned/' + i, "r", encoding="utf-8") as f:  # Open the cleaned file for reading
            content = f.read()  # Read the content of the file

            for k, v in dicoclean.items():  # Iterate through the dictionary and replace specific character sequences
                for j in v:
                    content = content.replace(j, k)

        with open('./cleaned/' + i, "w", encoding="utf-8") as f:  # Write the modified content back to the cleaned file
            f.write(content)


