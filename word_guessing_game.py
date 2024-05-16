# Word Guessing Game Program by Daniel Lee (baumpyru)
# Import modules for later use in program
import random
# Used to randomly pick a word
import csv
# Used to write scores to scores.csv
import plotscores
# Add my own module to plot scores

# Get player information (name)
name = input("Enter your name:")

# Tell player a quick intro to word guessing game
print(f"\nHello {name}, this game's premise is simple, guess a letter or the entire animal before you hit 25 tries.\nGetting to the lowest number wins!")
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

# Game code
def guess_word():
    word = randomanimal()
    tries = 0
    correct_guess = False
    guessed_word = "_" * len(word)
    print("\nWord to guess:", ' '.join(guessed_word))
    while not correct_guess and tries < 25:
        print(f"Tries left: {25 - tries}")
        guess = input("Guess a letter or the whole word:")
        if guess.lower() =="giveup":
            print("\n(╯°□°）╯︵ ┻━┻\nYou've given up! The animal was", word)
            return
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
            for i, char in enumerate(word):
                if char == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
            print("\nWord to guess:", ' '.join(guessed_word))
            print("You've correctly guessed a letter!")
        else:
            print("\nWord to guess:", ' '.join(guessed_word))
            print("Incorrect. Guess again!")
    
    if not correct_guess and guess.lower() != "giveup":
        print("Out of tries! The animal was", word)

# Save scores to scores.csv, newline is every entry and data layout is name, tries
    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, tries])
    
# Asks if player wants to see their and other player's scores
    while True:
        show_score = input("\nWould you like to see scores? (y/n):").lower()
        if show_score in ['y', 'n']:
            break
        else:
            print("\nInvalid input, please enter y or n")

    if show_score == "y":
        plotscores.plotscores()
    else:
        print(f"\nThanks for playing {name}!")

# Start program
if __name__ == "__main__":
    guess_word()