import random
import re
import time
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
    theme_choice = input('Pilih tema : ')
    
    if bool(re.compile(theme_choice).findall(str(tema))) : 
        word = get_word(tema[theme_choice])
        clear()
    
    else :
        print('tema '+ theme_choice + ' tidak ditemukan')
        print('exiting')
        time.sleep(1)
        exit()

    #definisiin macam macam var
    tries = 0 
    guessed_letter = []
    wrong_guessed_letter = []

    while tries != 8 :
        #print hangmannya
        print(hangman_list[tries])

        print('guessed letter : ' + str(guessed_letter))
        print('wrong letter : ' + str(wrong_guessed_letter))

        #kasih tau kata nya
        print('your word is : ' + word)
        player_guess = input('your letter guess : ').upper()
        #print(player_guess)

        if bool(re.compile(player_guess).search(word.upper())) and len(player_guess) == 1 : 
            print('you guessed 1 letter')
            guessed_letter.append(player_guess)

        elif len(player_guess) > 1 :
            print('invalid guess, try again!')
        
        else :
            print('you guessed wrong letter')
            tries = tries + 1
            wrong_guessed_letter.append(player_guess)
            
        time.sleep(0.5)
        
    if tries == 8 :
        clear()
        print ('you lose')
        print ('the word was : ' + word )
    else :
        clear()
        print('you win, you guessed the word')
    
    #play again?
    play_again = input('Play again? Y / N : ')
    if play_again == 'Y' or play_again == 'y': 
        clear()
        hangman()
    else :
        print('Thank you for playing!!!') 
        time.sleep(2)
        clear()

#mekanisme gamenya ydah tapi belum ditentukan kondisi menangnya gimana
#belum juga nunjukin _ _ _ _ sesuai length wordnya 


hangman()
