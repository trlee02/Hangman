import random 

words = open("/Users/trist/Desktop/Coding/PythonProjects/Hangman/words.txt", "r")

answer = random.choice(list(words))
incorr_guess = 0

cur_guesses = ["_"]*len(answer)


while incorr_guess < 6:
    guess = input("Guess a letter: ")
    if guess in answer:
        print("Correct! That is a letter in the word.")
        #get index where the char is in the string
        print(answer.find(guess))
        
    else:
        print("That is not a letter in the word")
        incorr_guess += 1

    print(*cur_guesses)
