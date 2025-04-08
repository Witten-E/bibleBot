"""
Take in the text and check for the words in it with the bible, calculate the ratio of how many times it shows up, 
and create a proper reply message.
Author: Eva Witten
"""
import bible, re

QUESTIONS = ["how much bible", "none of those words were in the bible", "biblebot", "nwib"]


# from dictCreation.py
def message_to_list(message):
    result = []
    # splits on words but includes words with apostrophes
    regex_gpt = r"\b[a-zA-Z']+(?!\w*\d)"
    return re.findall(regex_gpt, message.lower())
    


def find_ratio(message):
    count = 0
    words = message_to_list(message)
    not_in_bible = set()
    for word in words:
        word = word.strip(".'\"\\/!@#$%^&*()_+}{:<>?,`~|")
        if word in bible.BIBLE_DICT:
            count += 1
        else:
            not_in_bible.add(word)
    return count/len(words), not_in_bible

def generate_response(message):
    ratio, not_in_bible = find_ratio(message)
    if ratio == 0:
        return "That is correct! None of those words are in the bible"
    return f"Incorrect. {int(ratio*100)}% of those words were in the bible. The words not in the bible include {not_in_bible}." 
    


def main():
    pass

if __name__ == '__main__':
    main()