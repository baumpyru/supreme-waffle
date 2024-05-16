# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Get player information (name)
name = input("Enter your name:")

# Tell player a quick intro to word guessing game
print(f"Hello {name}, this game's premise is simple, guess the animal name or a letter before you run out of tries.\nYou start with 25 tries, getting to the highest number wins!")
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
#print(randomanimal())

# Game code
def guess_word():
    word = randomanimal()
    tries = 25
    correct_guess = False
    while not correct_guess and tries > 0:
        print(f"Tries left: {tries}")
        guess = input("Guess a letter or the whole word:")
        if guess.lower() =="giveup":
            print("(╯°□°）╯︵ ┻━┻\nYou've given up! The animal was", word)
            break
        tries -=1
        if guess.lower() == word.lower():
            print(''' 
                     ██████  ██████  ██████  ██████  ███████  ██████ ████████ ██ 
                    ██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██ 
                    ██      ██    ██ ██████  ██████  █████   ██         ██    ██ 
                    ██      ██    ██ ██   ██ ██   ██ ██      ██         ██       
                     ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██    ██''')
            print(f"Contratulations, you guessed the word in {tries} tries")
            correct_guess = True
        else:
            print("Incorrect. Guess again!")
    
    if not correct_guess and guess.lower() != "giveup":
        print("Out of tries! The animal was", word)

# Start program
guess_word()