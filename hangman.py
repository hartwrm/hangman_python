import random
import requests
import re

# print(fetch_words.json())
def hangman():
    fetch_words = requests.get("https://random-word-api.herokuapp.com/word?number=10")
    word = random.choice(fetch_words.json())
    print(word)
    turns = 10
    search = input("guess a word or letter\n")
    guess = re.findall(search, word)
    print(guess)


name = input("Enter your name\n")

print("Welcome" , name)
print("---------------")
print("Play hangman, you get 10 attempts to guess the word")

hangman()