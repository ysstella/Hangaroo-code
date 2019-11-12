def getGuessedWord(secretWord, letterGuessed):
    strg=''
    for char in secretWord:
        if char in letterGuessed:
            strg+=char
        else:
            strg+=('_')
    return strg