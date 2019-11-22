# --------------------------------------------------------------------------------------
# File: Exercise_8.1.py
# Name: Amie Davis
# Date: 7/25/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 8.1
#
# Purpose: Reads a text file and counts words and their occurrences.
#
# Usage: File to read must exist in same directory as Python program.
#        Outputs file to same directory.
#
# Functions: add_word(), process_line(), process_file(), main()
#
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# Adds each word and count to a dictionary
def add_word(word, word_dict):

    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

# --------------------------------------------------------------------------------------
# Splits each line into words
def process_line(line, word_dict):
    import string

    # Strips line of punctuation and case
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))

    # Splits each line into words and stores in a dictionary
    word_list = line.split()

    for word in word_list:
        add_word(word, word_dict)

# --------------------------------------------------------------------------------------
# Formats output
def process_file(word_dict, filename):

    # Sorts by descending counts
    # Converts dictionary to a tuple list with values listed first, then sorts
    # so count is now the first element in the list, whereas word is now the second element.
    tuple_list = list()
    for key, val in word_dict.items():
        tuple_list.append((val, key))
    tuple_list.sort(reverse=True)

    # Outputs words with count to file
    with open(filename, 'a') as fileHandler:

        fileHandler.write('\n')

        # Pads word field to 18 characters to align results
        for pair in tuple_list:

            count = pair[0]
            word = pair[1]

            fileHandler.write('{:18} {}'.format(word, count))
            fileHandler.write('\n')

# --------------------------------------------------------------------------------------
# Main program
# Opens file, calls functions to process each line and output results
# define main
def main():
    import os

    # Initializations
    word_dict = dict()

    # Opens read file
    try:
        getty_file = open('gettysburg.txt', 'r')

    except:
        print('File cannot be opened.')
        exit()

    # Processes each line and adds to word dictionary
    for line in getty_file:
        process_line(line, word_dict)

    # Finds number of words in dictionary
    word_count = len(word_dict)

    # Prompts user for output filename
    filename = input('Enter a file name for the output file.')

    # Check for previous existence of file
    if os.path.isfile(filename):
        overwrite = input('This file already exist.  Enter Y to overwrite the existing file.')

        if overwrite != 'Y':
            exit()

    # Creates header
    header1 = 'Length of the dictionary: ' + str(word_count)
    header2 = 'Word               Count '
    header3 = '-------------------------'

    # Output to file
    with open(filename, 'w') as fileHandler:

        fileHandler.write(header1)
        fileHandler.write('\n\n')
        fileHandler.write(header2)
        fileHandler.write('\n\n')
        fileHandler.write(header3)

    # Prints Dictionary
    process_file(word_dict, filename)

# --------------------------------------------------------------------------------------
# Runs program
main()