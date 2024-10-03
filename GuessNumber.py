import random

print("Enter a random number from 1 - 100, but you got only 3 changes.")

numToGuess = random.randrange(100)

changes = 3

guessCounter = 0

while guessCounter < changes:
