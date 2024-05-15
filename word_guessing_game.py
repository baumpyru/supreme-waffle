# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Get player information (name)
name = input("Enter your name:")

# Tell player a quick intro to word guessing game
# Test print by defining name
name = "UniqueName"
print(f"Hello {name}, this game's premise is simple, guess the animal name or a letter before you run out of tries.\nYou start with 25 tries, getting to the highest number wins.")
print(''' ██████   ██████   ██████  ██████      ██      ██    ██  ██████ ██   ██ ██ 
██       ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██  ██ 
██   ███ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      █████   ██ 
██    ██ ██    ██ ██    ██ ██   ██     ██      ██    ██ ██      ██  ██     
 ██████   ██████   ██████  ██████      ███████  ██████   ██████ ██   ██ ██''')

# Randomly choose word from wordbank
def randomanimal():
    with open('wordbank.txt','r') as file:
        words = file.readlines()
        return random.choice(words).strip()
# Test random word
# print(randomanimal())

# Game code
# def guess_word():
    


# Give player hint when requested