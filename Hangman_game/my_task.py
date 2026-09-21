import random
import time 
import os 
import requests

def show_welcome_message():

    print("----------- Welcome To The Hangman -----------")
    time.sleep(8) 
    print("Let's come inside the game") 

# show_welcome_message() 

def show_categories():

    # Categories = ['Nature', 'Science', 'Geography', 'Entertainment', 'Food', 'Lifestyle', 'Education', 'Difficulty']

    words_api = requests.get('https://api.apiverve.com/v1/hangmanword')

    if words_api == 200:
        words_data = words_api.json()
        return words_data 
    else:
        return f"Error: {words_api}"

def choose_category():
    choose_cate = input("Enter Your Category: ")
    
def pick_word():
    pass 

def display_initial_state(word_length, category):
    pass

print(show_categories())

# {
#   "status": "ok",
#   "error": null,
#   "data": {
#     "words": [
#       {
#         "word": "HOCKEY",
#         "blanks": "_ _ _ _ _ _",
#         "length": 6,
#         "uniqueLetters": 6,
#         "difficulty": "medium",
#         "category": "sports",
#         "maxGuesses": 6
#       }
#     ],
#     "count": 1,
#     "difficulty": "medium",
#     "category": "random",
#     "html": null
#   },
#   "premium": {
#     "message": "Unlock 1 additional field with a paid plan.",
#     "upgrade_url": "https://dashboard.apiverve.com/plans",
#     "locked_fields": [
#       "html"
#     ]
#   }
# }