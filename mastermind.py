# this game is an inspiration from 'tech with tim' yt channel - i did't see the actual code but i saw how it works and try to recreate the game on my own

import random
import re

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
LENTH_CODE = 4
MAX_TRIES = 10

def main():
    
    print(f"""
        WELCOME TO MASTERMIND  
        
        Attempt to guess the {LENTH_CODE} digit code...
        you have 10 tries.
        """)
    print('The colors that could make up the code are:', *COLORS)

    code = generate_code()
    tries = 0

    while tries < MAX_TRIES:
        crct_guess = 0
        incrct_guess = 0
        
        # increase the no of tries for each loop
        tries += 1

        guess = get_user_guess()
        
        if guess:
            for i in range(LENTH_CODE):
                if guess[i] == code[i]:
                    crct_guess += 1
                else:
                    incrct_guess += 1
        else:
            print('Invalid Guess!')
            continue
        
        if crct_guess == LENTH_CODE:
            print(f'You guessed the code in {tries} tries!')
            break
        else:
            print(f'Correct position: {crct_guess} | Incorrect possion: {incrct_guess}\n')
            
    # If user run out of tries - print code
    if tries == MAX_TRIES:
        print('You runout of tries :( \nThe code is', *code)          


def generate_code():
    # Create an code of {LENTH_CODE} random values from colors 
    code = [random.choice(COLORS) for _ in range(LENTH_CODE)]
    return code
            
            
def get_user_guess():
     # Get user guess and Validate it, return a list if valid, None if invalid
    guess = input('Guess (space seperated): ').strip().upper()
    
    if re.match(r'^[A-Z] [A-Z] [A-Z] [A-Z]$', guess):  
        # Check - All the user input charachters are valid colors    
        guess_list = [guess[i] for i in range(0, 7, 2) if guess[i] in COLORS]
        if len(guess_list) == LENTH_CODE:
            return guess_list

    return None


if __name__ == '__main__':
    main()