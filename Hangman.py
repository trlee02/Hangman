import random 

words = open("/Users/trist/Desktop/Coding/PythonProjects/Hangman/words.txt", "r")

answer = random.choice(list(words))
