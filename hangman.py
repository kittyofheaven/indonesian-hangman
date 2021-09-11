import random
import re
from wordlist import makanan, hewan
from os import system, name
from animation import hangman_list

#print(makanan)
#print(hewan)

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def get_word(player_choice):
    word = random.choice(player_choice)
    return word

def hangman():
    print("1. Makanan")
    print("2. Hewan")
    tema = {1 : makanan, 2 : hewan,}
    #print(tema[1])
    theme_choice = input('Pilih tema : ')
    word = get_word(tema[theme_choice])
    clear()
    print(word)

hangman()
