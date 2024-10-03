import random

print("Enter a random number from 1 - 100, but you got only 3 changes.")
print("Enter a random number from 1 - 5, but you got only 3 changes.")

numToGuess = random.randrange(100)
numToGuess = random.randrange(5)

changes = 3

guessCounter = 0

while guessCounter < changes:
    guessCounter += 1
    playerGuess = int(input('Please enter your guess: '))
    
    if playerGuess == numToGuess:
        print(f'Your guess is right in only {guessCounter}')
        break
    elif guessCounter >= changes and playerGuess != numToGuess:
        print(f'You ran out of guesses. The number was {numToGuess}.')

    elif playerGuess > numToGuess:
        print('Your guess is too high')

    elif playerGuess < numToGuess:
        print('Your guess is too low')