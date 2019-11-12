import string
def getAvailableLetters(lettersGuessed):
    strg = string.ascii_lowercase
    for char in lettersGuessed:
        if char in strg:
            strg = strg.replace(char, '')
    return strg