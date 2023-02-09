# this game is an inspiration from 'tech with tim' yt channel - i did't see the actual code but i saw how it works and try to recreate the game on my own

import random
import re

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
max_tries = 10

def main():
    
    print(""" 
        WELCOME TO MASTERMIND  
        
        Attempt to guess the 4 digit code...
        you have 10 tries.
        """)
    print(f'The colors that could make up the code are: R G B Y W O\n')

    code = [random.choice(COLORS) for _ in range(4)]
    tries = 0
    
    print(code)

    while tries < max_tries:
        crct_guess = 0
        incrct_guess = 0
        
        user_guess = input('Guess (space seperated): ')
        guess_list = validate_guess(user_guess)
        if guess_list:
            for i in range(4):
                if guess_list[i] == code[i]:
                    crct_guess += 1
                else:
                    incrct_guess += 1
        else:
            print('Invalid Guess')
            
        tries += 1
        
        if crct_guess == 4:
            print(f'You guessed the code in {tries} tries!')
            break
        else:
            print(f'Correct position: {crct_guess} | Incorrect possion: {incrct_guess}\n')
            
            
def validate_guess(guess):
    guess = guess.strip().upper()
    if re.match(r'^[A-Z] [A-Z] [A-Z] [A-Z]$', guess):  
            
        guess_list = [guess[i] for i in range(0, 7, 2) if guess[i] in COLORS]
        
        if len(guess_list) == 4:
            return guess_list
        else:
            return None
    else:
        return None
    
if __name__ == '__main__':
    main()