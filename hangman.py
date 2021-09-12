import random
import re
import time
import string
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

def split(word):
    return [char for char in word]

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
    question = {}
    word_completion = '_' * len(word)
    list_word_completion = split(word_completion)
    list_word = split(word.upper())

    while tries != 8 and list_word != list_word_completion :
        #print hangmannya
        print(hangman_list[tries])

        print('guessed letter : ' + str(guessed_letter))
        print('wrong letter : ' + str(wrong_guessed_letter))

        #kasih tau kata nya
        wordo_completion = ''.join(list_word_completion)
        print('your word is : ' + wordo_completion)
        
        if bool(re.compile(word[0].upper()).search(wordo_completion)) == False :

            player_guess = word[0].upper()
            for idx, item in enumerate(list_word):
                if player_guess in item:
                    list_word_completion[idx] = player_guess
            guessed_letter.append(player_guess)

        else :

            player_guess = input('your letter guess : ').upper()

            if bool(re.compile(player_guess).search(word.upper())) and len(player_guess) == 1 : 
                
                if player_guess in guessed_letter :
                    print("you already guessed " + player_guess)
                else :
                    for idx, item in enumerate(list_word):
                        if player_guess in item:
                            list_word_completion[idx] = player_guess

                    print('you guessed 1 letter')
                    guessed_letter.append(player_guess)

            elif len(player_guess) > 1 :
                print('invalid guess, try again!')
            
            else :
                if player_guess in wrong_guessed_letter :
                    print("you already guessed " + player_guess)
                else :
                    print('you guessed wrong letter')
                    tries = tries + 1
                    wrong_guessed_letter.append(player_guess)
                
            time.sleep(0.5)
        
    if tries == 8 and list_word != list_word_completion:
        clear()
        print ('you lose, you guessed the word, the word was ' + word)
    else :
        clear()
        print('you win, you guessed the word, the word was ' + word)
    
    #play again?
    play_again = input('Play again? Y / N : ')
    if play_again == 'Y' or play_again == 'y': 
        clear()
        hangman()
    else :
        print('Thank you for playing!!!') 
        time.sleep(2)
        clear()

hangman()
