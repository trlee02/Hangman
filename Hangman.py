import random 
import re

words = open("/Users/trist/Desktop/Coding/PythonProjects/Hangman/words.txt", "r")

answer = random.choice(list(words))
incorr_guess = 0

cur_guesses = ["_"]*(len(answer)-1)

def printGuesses(guess, answer):
    #count = 0
    index = []

    for i in range(len(answer)):
        if answer[i] is guess:
            cur_guesses[i] = guess 

    return index
            
    

while incorr_guess < 6:
    guess = input("Guess a letter: ")
    if guess in cur_guesses:
        print("\nYou have already guessed \"{}\"".format(guess))
    elif guess in answer:
        print("\nCorrect! That is a letter in the word.\n")
        #get index where the char is in the string
        printGuesses(guess, answer)
    else:
        print("\nThat is not a letter in the word\n")
        incorr_guess += 1

    print(*cur_guesses)
    print("")

print("\nThe correct answer is " + answer)

#  O 
# /|\
# / \
