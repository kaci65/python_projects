#!/usr/bin/python3
"""Guessing number game"""


import random

secret_num = random.randint(1, 20)
chances_left = 5

print("Hello there! Please choose a number between 1 and 20")
for i in range(0, chances_left):
    while True:
        try:
            guess_num = int(input("Enter a number: "))
            break
            print()
        except ValueError:
            print("Please enter a number!")

    if guess_num < secret_num:
        print("Your guess is too low")
    elif guess_num > secret_num:
        print("Your guess is too high")
    else:
        break

    chances_left = chances_left - 1
    print(f"You have {chances_left} chances left")
    print()

if guess_num == secret_num:
    print("You've won!")
else:
    print("You lose!")

print()
print(f"The secret number was {secret_num}")
