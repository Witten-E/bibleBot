"""
This file is designed to process a txt file and create a new text file that contains a dictionary of all the 
words (in lowercase) in the original file and their count
Author: Eva Witten
"""

import sys, re


def message_to_list(message):
    result = []
    # splits on words but includes words with apostrophes
    regex = r"[^\d\W]+('\w)?"
    regex_gpt = r"\b[a-zA-Z']+(?!\w*\d)"
    return re.findall(regex_gpt, message.lower())
    


def process_file(filename):
    '''
    iterates through the file to create a dictionary of all the words inside them
    '''
    words = {}
    with open(filename) as file:
        for line in file:
            # for c in line: # replaces special characters with spaces
            #     new_line = ''
            #     for c in line:
            #         if c.isalpha():
            #             new_line += c
            #         else:
            #             new_line += ' '
            # line = new_line.lower().split() # splits the line into a list of lowercase words 
            line = message_to_list(line)               
            for word in line:  # adds the word to the dictionary
                if not word in words.keys():
                    words[word] = 1
                else:
                    words[word] += 1
        return words


def main():
    # args = sys.argv[1:]
    # if len(args) == 0:
    #     filename = "bibleTxts/bibleTestDocs/bible.txt"
    # elif len(args)>1:
    #     startdir = args[1]
    #     file_write_to = startdir + "dictionaries/" + filename
    # else:
    #     file_write_to = "dictionaries/" + filename
    # filename = args[0]
    filename = "bible.txt"
    words = process_file("bibleTxts/bibleTestDocs/" + filename)
    file_write_to = "bibleTxts/" + filename
    
    with open(file_write_to, "w") as file:
        file.write("{\n")
        for word in words:
            file.write(f'"{word}\": {words[word]},\n')
        file.write("}")

if __name__ == '__main__':
    main()