
def anti_vowel(text):
    new_text = ""      # this is a variable to hold the new text without vowels
    for letter in text:
        if letter not in ('aeiouAEIOU'):   # check if letter is not a vowel
            new_text += letter    # if letter is not a vowel add it to new_text
    return new_text