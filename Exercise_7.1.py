# --------------------------------------------------------------------------------------
# File: Exercise_7.1.py
# Name: Amie Davis
# Date: 7/18/2019
# Course: DSC510 - Introduction to Programming
# Assignment Number: 7.1
#
# Purpose: Reads a text file and counts words and their occurrences.
#
# Usage: File to read must exist in same directory as Python program.
#
# Functions: add_word(), process_line(), pretty_print(), main()
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
def pretty_print(word_dict):

    # Finds number of words in dictionary
    word_count = len(word_dict)

    # Prints header
    print('\n')
    print('Length of the dictionary: {}'.format(word_count))
    print('\n')
    print('Word               Count ')
    print('-------------------------')

    # Sorts by descending counts
    # Converts dictionary to a tuple list with values listed first, then sorts
    # so count is now the first element in the list, whereas word is now the second element.
    tuple_list = list()
    for key, val in word_dict.items():
        tuple_list.append((val, key))
    tuple_list.sort(reverse=True)

    # Outputs word with count
    # Pads word field to 16 characters to align results
    for pair in tuple_list:
        print('{0[1]:16} {0[0]}'.format(pair))

# --------------------------------------------------------------------------------------
# Main program
# Opens file, calls functions to process each line and output results
# define main
def main():

    # Initializations
    word_dict = dict()

    # Opens file
    try:
        getty_file = open('gettysburg.txt', 'r')

    except:
        print('File cannot be opened.')
        exit()

    # Processes each line and adds to word dictionary
    for line in getty_file:
        process_line(line, word_dict)

    # Prints Dictionary
    pretty_print(word_dict)

# --------------------------------------------------------------------------------------
# Runs program
main()