#Game: Guess the number
#Rodrigo Banos Hernandez
logo = """                            
 ______    _______  ______   __   _______    _______  _______  __   __  _______  ___                             
|    _ |  |       ||      | |  | |       |  |       ||   _   ||  |_|  ||       ||   |                            
|   | ||  |   _   ||  _    ||__| |  _____|  |    ___||  |_|  ||       ||    ___||___|                            
|   |_||_ |  | |  || | |   |     | |_____   |   | __ |       ||       ||   |___  ___                             
|    __  ||  |_|  || |_|   |     |_____  |  |   ||  ||       ||       ||    ___||   |                            
|   |  | ||       ||       |      _____| |  |   |_| ||   _   || ||_|| ||   |___ |___|                            
|___|  |_||_______||______|      |_______|  |_______||__| |__||_|   |_||_______|                                 
 _______  __   __  _______  _______  _______    _______    __    _  __   __  __   __  _______  _______  ______   
|       ||  | |  ||       ||       ||       |  |   _   |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
|    ___||  | |  ||    ___||  _____||  _____|  |  |_|  |  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
|   | __ |  |_|  ||   |___ | |_____ | |_____   |       |  |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
|   ||  ||       ||    ___||_____  ||_____  |  |       |  |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |  |   _   |  | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|  |__| |__|  |_|  |__||_______||_|   |_||_______||_______||___|  |_| """

import random
import os
os.system("clear")

#Additional Functions---------------------------------------------------------------------------------------------------------------------
def compare_numbers(guess, mystery_number):
    """Tells you if you guessed correctly, lower or higher"""
    if guess == mystery_number:
        return "You guessed right, you win! 😎"
    elif guess > mystery_number and (guess - mystery_number) > 10:
        return "You're too high 🤨"
    elif guess > mystery_number and (guess - mystery_number) <= 10:
        return "You're close, go lower 😯"
    elif guess < mystery_number and (mystery_number - guess) > 10:
        return "You're too low 🤨"
    elif guess < mystery_number and (mystery_number - guess) <= 10:
        return "You're close, go higher 😯"

def game_over(mystery_number, guess_list, attempts):
    """Determines if the user has guessed the number or has ran out of attempts"""
    if mystery_number in guess_list:
        return True
    elif len(guess_list) >=  attempts:
        return True
    else:
        return False
    
#Main Function Start--------------------------------------------------------------------------------------------------------------------
def guess_a_number():

    print(logo)
    print("\nLet's play a game.\nGuess the number I'm thinking!\nBetween 1 and 100")

    #variables------------------------------------------------------------------------
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'(default): ").lower()
    guess_list = []
    mystery_number = random.randint(0,100)
    guess = 0
    attempts = 0

    #assigning a number of attempts depending on the chosen difficulty-------------------------
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    #Checking if the game has ended------------------------------------------------------------
    
    while not game_over(mystery_number=mystery_number, guess_list=guess_list, attempts=attempts):
        
        #Filling the list of guesses:
        guess = int(input("Make a guess: "))
        guess_list.append(guess)
        #Comparing the Mystery Number vs the user's Guess:
        print(compare_numbers(guess=guess, mystery_number=mystery_number))
        #Calculating the number of attempts left:
        attempts_left = attempts - len(guess_list)
        #Checking if the user has won or lost:
        if mystery_number not in guess_list:
            os.system("clear")
            print(f"You have {attempts_left} attempts left. Guess again")
            print(f"Your guesses: {guess_list}")
            #print(f"Mystery Number: {mystery_number}") #To check while you debug

        elif len(guess_list) >=  attempts and mystery_number not in guess_list:
            print("You ran out of attempts, you lose... 😭") 
#Main Function End---------------------------------------------------------------------------------------------

#Game Loop---------------------------------------------------------------------------------------------------------------------------------------

guess_a_number()
while input("Do you want to play again? y/n: ").lower() == "y":
    os.system("clear")
    guess_a_number()
