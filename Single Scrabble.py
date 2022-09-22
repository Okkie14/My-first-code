# Scrabble Game
# Random for a random letter
#Time for sleep to delay the between turns
#CSV for the scoreboard

import random
import time as t
import csv

#Letters and values for each letter that can be used in scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Dictionary for letters to points assigning a key value to letters and points
letter_to_points = {
    key: value 
    for key, value
    in zip(letters, points)
}

player_score = 0 #Keep track of the players score using the score function
word_list = [] #List to append words to
word_list_score = [] #List to score the word played
counter = 0 #Counting how long it takes to reach 100 points

#List to store all words played
def words_played(word):
    global word_list
    word = word.upper()
    word_list.append(word)
    word_list_score.append(word)
    return word_list

#Scoring of each word 
def score(word_list):
    global player_score
    total = 0
    for letter in word_list_score:
        for let in letter:
            total += letter_to_points.get(let, 0)
    word_list_score.pop()
    player_score += total
    return player_score

def top_five():
    all_scores = []

    with open(r'C:\Users\okker\Documents\Personal\Coding\Programmes\Single Scrabble\scoreboard.csv', newline = '') as csvfile:
        scores = csv.reader(csvfile)

        for row in scores:
            all_scores.append(row)

    top = sorted(all_scores, key=lambda a: int(a[0]))
    print(top[:5])
    

#Game play function
def game_play():
    global counter
    while player_score <= 150:
        your_letter = random.choice(letters)
        print(player + ', your word should start with: ' + your_letter)
        word = input()
        t.sleep(2)
        #Scrabbel Dictionary to see if you played a valid word
        with open(r'C:\Users\okker\Documents\Personal\Coding\Programmes\Single Scrabble\scrabble_dictionary.txt','r') as s_dict:
            if word.upper() in s_dict.read():
                if word[0].upper() == your_letter:
                    print(words_played(word))
                    score(word_list)
                    print('Current score is ' + str(player_score))
                    t.sleep(1)
                else:
                    print('Your word did not start with the correct letter')
                    continue
            else:
                print('That is not a real word')
                continue
        counter += 1
        if player_score >= 150:
            print('It took ' + str(counter) + ' turns to win the game')
            t.sleep(2)
            top_five()

        else:
            continue
        
        with open(r'C:\Users\okker\Documents\Personal\Coding\Programmes\Single Scrabble\scoreboard.csv', 'a', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow([int(counter), player])

#To get username, create scoreboard with username2
player = input('What is your name? ')

print(
    """
The game will continue until you have reached a 100 points.
Your score will show after each round.
Scoreboard will be updated after you reached a 100 points.
Can you be part of the top 5!
Good luck! :-)
    """
)
t.sleep(4)
#Game play
print('Please select 1 to play')
print('Please select 2 to see the top 5 players')
print('Please select 3 to exit')
ans = input()

if int(ans) == 1:
    game_play()
elif int(ans) == 2:
    top_five()
    print('Would you like to try and beat the top scorer? Press 1 to try or 2 to exit')
    ans = input()
    if int(ans) == 1:
        game_play()
    else:
        exit()
else:
    'Thank you for playing'
    exit()