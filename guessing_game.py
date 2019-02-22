"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

FERNANDO URIEL WERTT RETA

"""
    
import random
record = []

def start_game():
    print(""" 
        ------------------------------------
        Welcome to the Number Guessing Game!
        ------------------------------------
        """)
    answer = random.randint(1, 10)
    guess = input("Pick a number between 1 and 10: ")
    attempts = 1
    
    while answer != guess:
        try:
            guess = int(guess)
        except ValueError:
            print("Thats not a number")
            guess = input("Pick a number between 1 and 10: ")
            attempts += 1
        if guess < answer:
            print("It's higher")
            guess = input("Pick a number between 1 and 10: ")
            attempts += 1
        elif guess > answer:
            print("It's lower")
            guess = input("Pick a number between 1 and 10: ")
            attempts += 1
    print("NICE! You scored in {} attemps".format(attempts))
    record.append(attempts)
    print("Your scores is: {}".format(attempts))
    score = print("The best record is : {} attempts".format(min(record)))
    play_again = input("Do you want to play again? ([y]es, [n]o) ")
    if play_again.lower() == 'y':
        start_game()
    else:
        print("GOOD BYE!!")
        print("The best record is : {} attempts".format(min(record)))

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
