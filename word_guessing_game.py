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

# why is it important to strip newline characters from the words read from the wordbank file before returning them in the random animal function?


# Give player hint when requested
