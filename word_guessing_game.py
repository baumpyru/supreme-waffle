# Word Guessing Game Program by Daniel Lee
# Import modules for later use in program
import random

# Get player information (name)
name = input("Enter your name:")

# Tell player a quick intro to word guessing game
print(f"Hello {name}, this game's premise is simple, guess a letter or the entire animal before you hit 25 tries.\nGetting to the lowest number wins!")
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
    tries = 0
    correct_guess = False
    guessed_word = "_" * len(word)
    print("Word to guess:", ' '.join(guessed_word))
    while not correct_guess and tries < 25:
        print(f"Tries left: {25 - tries}")
        guess = input("Guess a letter or the whole word:")
        if guess.lower() =="giveup":
            print("(╯°□°）╯︵ ┻━┻\nYou've given up! The animal was", word)
            break
        tries +=1
        if guess.lower() == word.lower():
            print(''' 
 ██████  ██████  ██████  ██████  ███████  ██████ ████████ ██ 
██      ██    ██ ██   ██ ██   ██ ██      ██         ██    ██ 
██      ██    ██ ██████  ██████  █████   ██         ██    ██ 
██      ██    ██ ██   ██ ██   ██ ██      ██         ██       
 ██████  ██████  ██   ██ ██   ██ ███████  ██████    ██    ██''')
            print(f"Congratulations, you guessed the word in {tries} tries")
            correct_guess = True
        elif len(guess) == 1 and guess in word:
            print("You've correctly guessed a letter!")
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
            print("Word to guess:", ' '.join(guessed_word))
        else:
            print("Incorrect. Guess again!")
    
    if not correct_guess and guess.lower() != "giveup":
        print("Out of tries! The animal was", word)

# Start program
if __name__ == "__main__":
    guess_word()