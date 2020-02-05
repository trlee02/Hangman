import random 

words = open("words.txt", "r")

print(random.choice(list(words)))