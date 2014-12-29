def censor(text, word):
    rep = '*' * len(word)
    return text.replace(word, rep)

"""
OR
def censor(text, word):
    split_text = text.split()
    word_sub = '*' * len(word)
    for x in split_text:
        if x == word:
            split_text[split_text.index(x)] = word_sub
    return " ".join(split_text)
"""
"""
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack") 

should return

"this **** is wack ****"

    Assume your input strings won't contain punctuation or upper case letters.
    The number of asterisks you put should correspond to the number of letters in the censored word.
"""