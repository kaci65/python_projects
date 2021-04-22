#!/usr/bin/python3
#  dice roll simulator using random()
import random

# Define infinite loop
while True:

    def roll_the_dice(dice):
        # Define the function that prints output based on dice value
        print("Dice: ", dice)

    # Generate a random number between 1 and 6
    # Call the function
    roll_the_dice(random.randint(1, 6))
    print()

    # Ask if user wants to roll dice again
    ques = input("Do you want to roll the dice again(y/n)? : ")
    # Terminate loop if user type anything apart from 'y'
    answer = ["yes", "y", "YES", "Y"]
    if ques not in answer:
        exit(0)
