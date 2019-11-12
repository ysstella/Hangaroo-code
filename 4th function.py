import time
import string

def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:      
        if char not in lettersGuessed:
           return False   
    return True

def getGuessedWord(secretWord, letterGuessed):
    strg=''
    for char in secretWord:
        if char in letterGuessed:
            strg+=char
        else:
            strg+=('_')
    return strg

def getAvailableLetters(lettersGuessed):
    strg = string.ascii_lowercase
    for char in lettersGuessed:
        if char in strg:
            strg = strg.replace(char, '')
    return strg

def Hangaroo(secretWord):
    name = input("What is your name? ")
    print ("Hello, " ,name, "Time to play Hangaroo!")
    time.sleep(0.5)
    print ("Start guessing...")
    time.sleep(0.5)

    turns = 4
    lettersGuessed=[]
    CurrAva=""
    PreAva=""
    CurrLG=getGuessedWord(secretWord, lettersGuessed)
    PreLG=CurrLG
    while turns > 0:
        guess= input("Guess a character: ")
        guess=guess.lower()
        lettersGuessed.append(guess)
        CurrAva=getAvailableLetters(lettersGuessed)
        if CurrAva==PreAva:
            print("You already used the character!")
            continue
        PreAva=CurrAva
        CurrLG=getGuessedWord(secretWord, lettersGuessed)
        if PreLG==CurrLG:
            print("The character you choose is wrong")
        print("Current guess is: ",CurrLG)
        
        if isWordGuessed(secretWord, lettersGuessed):
            return print("Congratulations! You've guessed the word!")
            
        if guess not in secretWord:  
            turns -= 1        
            print ("Try Again!")
            print( "You have", + turns, 'guesses left') 
 
    if turns == 0:           
        return print ("You Lose")
            