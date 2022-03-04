import requests
from typing import List
import random


#all letters
alphabet = "abcdefghijklmnopqrstuvwxyz"
#already used letters
usedLetters = []
#blank spaces and fill letters
game_board = []
#fetch random word
randomWord = requests.get("https://random-word-api.herokuapp.com/word?number=10").json()
word = random.choice(randomWord)

#Helps print current word being guessed
def print_game_board(letter: List):
    print("Guessing: {0}".format(" ".join(letter)))

#show number of guesses taken
def guesses_taken(current: int, total: int):
    print("you are on guess {0}/{1}".format(current, total))

#Welcome to the game
def welcome():
    name = input("Enter your name\n")
    print("Welcome" , name)
    print("---------------")
    print("Play hangman, you get 10 attempts to guess the word.")
    print(word)
    

#prep secret word for gameplay
def prep_word():
    word = random.choice(randomWord)
    for character in word:
        game_board.append("_")
    print("You can only guess a single letter at a time")
    print("The word contains", len(word), " letters")
    print_game_board(game_board)

#guessing the word 
def guess_word():
    #set turns variable
    turns = 1
    max_turns = 10
    while turns < max_turns:
        guess = input("Guess a letter\n").lower()
        if not guess in alphabet:  #check for valid input
            print("Enter a letter from a-z")
        elif guess in usedLetters: #has letter been used
            print("you already guessed that letter")
        else:
            usedLetters.append(guess)
            if guess in word:
                print("good guess!")
                for i in range (0, len(word)):
                    if word[i] == guess:
                        game_board[i] = guess
                print_game_board(game_board)
                guesses_taken(turns, max_turns)
                if not "_" in game_board:
                    print("You won! Congratulations")
                    break
            else:
                print("That letter is not in the word, guess again")
                turns += 1
                guesses_taken(turns, max_turns)
                if turns == 10:
                    print("Loser, the secret word was " + word)

#play again?
def play_again():
    replay = input("Play again? Y/N?\n").lower()
    if replay == 'y':
        hangman()
    else:
        print("See you next time.")

#run the game
def hangman():
    randomWord = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()
    word = randomWord[0]
    welcome()
    prep_word()
    guess_word()
    play_again()

hangman()