# 1. Name: 
#    Brandon Petersen
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Asks user for a max value and chooses a random number in between 1 and the max. then asks them to guess what the random number is.
# 4. What was the hardest part? Be as specific as possible.
#    I had a hard time changing the data types of the values i was printing. i kept forgetting to change them and i also made them the wrong type sometimes.
# 5. How long did it take for you to complete the assignment?
#    It took about a two hours to complete.   

import random

# Game introduction.

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Choose a positive integer: "))
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")
# Initialize the sentinal and the array of guesses.
guess = 0
guess_list = []
# Play the guessing game.
while(guess != value_random):
    
    # Prompt the user for a number.
    guess = int(input())
    
    # Store the number in an array so it can be displayed later.
    guess_list.append(guess)

    # Make a decision: was the guess too high, too low, or just right.
    if guess > value_random:
        print(" Too High!")
    if guess < value_random:
        print(" Too Low!")    
# Give the user a report: How many guesses and what the guesses where.
print(f"You took {len(guess_list)} guesses to find the number {value_random}.")
print(f"The numbers you guessed were {guess_list}.")