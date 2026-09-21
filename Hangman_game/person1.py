import json
import random

with open("words.json", "r") as file:
    words = json.load(file)

category = random.choice(list(words.keys()))
word = random.choice(words[category])

print("Category:", category)
print("Word:", "_" * len(word))