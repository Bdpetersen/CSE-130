# 1. Name: 
#    Brandon Petersen
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random

# Game introduction.

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Choose a positive integer: "))
# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print("Guess a number between 1 and " + str(value_max) + ".")
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
        print("Too High!")
    if guess < value_random:
        print("Too Low!")    
# Give the user a report: How many guesses and what the guesses where.
print("You took "+str(len(guess_list))+" guesses to find the number "+str(value_random))
print("The numbers you guessed were " + str(guess_list))