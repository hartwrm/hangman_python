import random
import requests
import re


#Welcome to the game
def welcome():
    name = input("Enter your name\n")
    print("Welcome" , name)
    print("---------------")
    print("Play hangman, you get 10 attempts to guess the word.")

#play again?
def play_again():
    replay = input("Play again? Y/N?\n").lower()
    if replay == 'y':
        hangman()
    else:
        print("See you next time.")

#run the game
def hangman():
    #call welcom to start game play
    welcome()

    #fetch random word, print hint
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1").json()
    print(word[0])
    print("The word contains", len(word[0]), " letters")
    print(len(word[0])*' _')

    #set turns variable
    turns = 10

    #already guess letters dictionary
    used_letters = []

    #get user input for word or letter
    search = input("guess a word or letter\n")
    
    #use regex matching to search word
    guess = re.findall(search, word[0])
    print(guess)

    play_again()




hangman()