import random 
import time
import os
import json

with open('Hangman_game/words.json', 'r') as f:
    categories = json.load(f)

def show_welcome_message():

    print("============================================")
    print("----------- Welcome To The Hangman ---------")
    print("============================================")
    time.sleep(8) 
    # os.system('cls')
    print("\033[H\033[J", end="")
    print("Let's come inside the game") 

show_welcome_message()

def show_categories():

    idx = 1
    for c in categories.keys():
        print(f"{idx}. {c}")
        idx += 1
    
show_categories()

def choose_category():

    global user_category
    global word
    user_category = input("Enter Word Category : ")
    os.system('cls')
    if user_category in categories:
        word = random.choice(categories[user_category])
        # print(user_category)
        print("============================================")
        print(f"Category :-> {user_category}")
        print(f"Word {len(word)}: ","_"*len(word))
        print("============================================")
    else:
        category = random.choice(list(categories.keys()))
        word = random.choice(categories[category])
        print("============================================")
        print(f"Category :-> {category}")
        print(f"Word {len(word)}: ","_"*len(word))
        print("============================================")

choose_category()


def draw_hangman():
    hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
    ]

    changes = 6
    drop = 0 
    word_length = len(word)
    while drop <= changes:
        user_input = input("Enter character of word :-> ")
        if len(user_input) > 1 :
            print("You need to write only one character")
        elif len(user_input) == 0:
            print("Please Enter the character value")
        else:
            if user_input not in word:
                print(hangman_stages[drop])
                drop += 1
            else:
                word_length -= 1
                if word_length == 0:
                    print("The word is :-> ",word)
                    break

draw_hangman()