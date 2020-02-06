import random 
import re

words = open("/Users/trist/Desktop/Coding/PythonProjects/Hangman/words.txt", "r")

answer = random.choice(list(words))
incorr_guess = 0

cur_guesses = ["_"]*len(answer)

def printGuesses(guess, answer):
    #count = 0
    index = []

    for i in range(len(answer)):
        if answer[i] is guess:
            cur_guesses[i] = guess 

    return index
            
    

while incorr_guess < 6:
    guess = input("Guess a letter: ")
    if guess in answer:
        print("Correct! That is a letter in the word.")
        #get index where the char is in the string
        printGuesses(guess, answer)

    else:
        print("That is not a letter in the word")
        incorr_guess += 1

    print(*cur_guesses)

print("\nThe correct answer is " + answer)
