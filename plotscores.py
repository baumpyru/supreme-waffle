# Word Guessing Game Program by Daniel Lee (baumpyru)
# This is a module imported into the main game
import csv
# Import csv to read scores.csv
import matplotlib.pyplot as plt
# Import matplotlib to plot scores

# Plot scores from scores.csv
def plotscores():
    names = []
    scores = []
    with open('scores.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
                name, score = row
                names.append(name)
                scores.append(int(score))
    plt.bar(names, scores)
    plt.xlabel('Player Name')
    plt.ylabel('Tries(Lower the better)')
    plt.title('Word Guessing Game Scores')
    plt.ylim(0, 25)
    plt.show()

plotscores()