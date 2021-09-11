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
    
    #pilihan tema
    tema = {'1' : makanan, 'makanan' : makanan, 'Makanan' : makanan, 
            '2' : hewan,'hewan' : hewan, 'Hewan' :hewan
            }
    
    #ambil kata
    theme_choice = raw_input('Pilih tema : ')
    word = get_word(tema[theme_choice])
    clear()
    
    #definisiin tries
    tries = 0 

    while tries != 8 :
        #print hangmannya
        print(hangman_list[tries])

        #kasih tau kata nya
        print('your word is : ' + word)
        player_guess = raw_input('your letter guess : ').upper()
        print(player_guess)

        if bool(re.compile(player_guess).search(word.upper())) : 
            print('you guessed 1 letter')
        
        else :
            print('you guessed wrong letter')
            tries = tries + 1

    if tries == 8 :
        print ('you lose')
        print ('the word was : ' + word )
    else :
        print('you win, you guessed the word')


hangman()
