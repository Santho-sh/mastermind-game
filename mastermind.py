# this game is an inspiration from 'tech with tim' yt channel - i did't see the actual code but i saw how it works and try to recreate the game on my own

import random
import re

def main():
    colors = ['R', 'G', 'B', 'Y', 'W', 'O']
    guess = 3

    print(""" 
        WELCOME TO MASTERMIND  
        
        Attempt to guess the 4 digit code...
        you have 10 tries.
        """)
    print(f'The colors that could make up the code are: R G B Y W O')

    code = []
    for _ in range(4):
        code.append(random.choice(colors))

    print(code)

    while guess > 0:
        crt_guess = 0
        incrt_guess = 0
        
        user_guess = input('Guess (space seperated): ')
        if validate_guess(user_guess):
            print('valid')
        else:
            print('Invalid Guess')
            
        guess -= 1
        
def validate_guess(guess):
    guess = guess.strip().upper()
    if re.match(r'^[A-Z] [A-Z] [A-Z] [A-Z]$', guess):
        
        guess_list = [guess[i] for i in range(0, 7, 2)]
        
        print(guess_list)
        return True
    else:
        return False
    
if __name__ == '__main__':
    main()