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

    # Create an code of 4 random values from colors 
    code = [random.choice(COLORS) for _ in range(4)]
    tries = 0

    while tries < max_tries:
        crct_guess = 0
        incrct_guess = 0
        
        # increase the no of tries for each loop
        tries += 1
        
        user_guess = input('Guess (space seperated): ')
        guess_list = validate_guess(user_guess)
        
        if guess_list:
            for i in range(4):
                if guess_list[i] == code[i]:
                    crct_guess += 1
                else:
                    incrct_guess += 1
        else:
            print('Invalid Guess!')
            continue
        
        if crct_guess == 4:
            print(f'You guessed the code in {tries} tries!')
            break
        else:
            print(f'Correct position: {crct_guess} | Incorrect possion: {incrct_guess}\n')
            
    # If user run out of tries - print code
    if tries == max_tries:
        print(f'You runout of tries :( \nThe code is {code}')          

            
def validate_guess(guess):
    # Validate user input and return a list if valid, none if invalid
    guess = guess.strip().upper()
    
    if re.match(r'^[A-Z] [A-Z] [A-Z] [A-Z]$', guess):  
        # Check - All the user inpu charachters are valid colors    
        guess_list = [guess[i] for i in range(0, 7, 2) if guess[i] in COLORS]
        if len(guess_list) == 4:
            return guess_list

    return None


if __name__ == '__main__':
    main()