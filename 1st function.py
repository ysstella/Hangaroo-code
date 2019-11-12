def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:      
        if char not in lettersGuessed:
           return False   
    return True