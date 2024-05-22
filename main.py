"""

@Author: Lex
@Date: 2024-05-23
@Description: This script reads a text file and displays the top n words in a bar chart.

@Usage: python main.py -n <number> of items to display
@Example: python main.py -n 15

"""


import requests
import json
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import sys

words = {}
displayCount = 10

if (len(sys.argv) > 1):
    if sys.argv[1] == "-n":
        displayCount = int(sys.argv[2])
else:
    print("Please run the script with -n <number> of items to display\ne.g. python main.py -n 15\nUsing default value of 10")
    
with open("text.txt", "r") as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            word = ''.join(e for e in word if e.isalnum())
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
words = dict(list(words.items())[:displayCount])

plt.bar(words.keys(), words.values())
plt.show()