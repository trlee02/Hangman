import random 

words = open("/Users/trist/Desktop/Coding/PythonProjects/Hangman/words.txt", "r")

print(random.choice(list(words)))