"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random

def start_game():
    # This is the welcome message with instructions as to how to play the game.
    print("""
                           (0)
    ===================== {000} =====================
                           (0)
     _    _              _______ _
    | |  | |            |__   __| |
    | |__| | ___ _   _     | |  | |__   ___ _ __ ___
    |  __  |/ _ \ | | |    | |  | '_ \ / _ \ '__/ _ \\
    | |  | |  __/ |_| |    | |  | | | |  __/ | |  __/
    |_|  |_|\___|\__, |    |_|  |_| |_|\___|_|  \___|
                  __/ |
                 |___/ 
                           (0)
    ===================== {000} =====================
                           (0)
                           
    Welcome to the number guessing game! I'll pick a
    numer between 1 and 10 and you'll guess it. Don't
    worry! I'll give you hints along the way. Try to
    do this in the lowest number of tries possible! 
    GOOD LUCK!
    """)
    
    random_number = random.randrange(1, 10)
    tries = 0
    highscore = 0
    
    while True:
        try:
            answer = int(input('Guess:  '))
            
            if answer == random_number:
                tries += 1
                print("Congratulations! You've won!")
                print(f'Your score is: {tries}')
                if highscore == 0 or tries < highscore:
                    highscore = tries
                    print('You got the highscore!')
                          
                # This will check if the player wants to keep playing.
                play_again = input('Would you like to play again? (Y/N)  ')
                if play_again.lower() == 'y' or play_again.lower() == 'yes':
                    
                    # This resets values and spits out the highscore.
                    tries = 0
                    random_number = random.randrange(1, 10)
                    print(f'\nThe highscore is {highscore}.\nGood luck!')
                    continue
                else:
                    break
            
            # If they input a number outside the range, it will give a message.
            elif answer > 10 or answer < 1:
                tries += 1
                print("You've gone off the map! Try again between 1-10")
                continue
            elif answer > random_number:
                tries += 1
                print("It's lower!")
                continue
            elif answer < random_number:
                tries += 1
                print("It's higher!")
                continue
                
        # If they input a letter, word, or float, the loop will reset with a message.
        except ValueError:
            print("We need a whole number between 1-10. Please try again!")
            continue

# Kick off the program by calling the start_game function.
start_game()
print('Thank you so much for playing my game!')