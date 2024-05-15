# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Randomly choose word from wordbank
def randomanimal():
    with open('wordbank.txt','r') as file:
        words = file.readlines()
        return random.choice(words)

# Test random word
print(randomanimal())

#


# Give player hint when requested
