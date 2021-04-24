#!/usr/bin/python3
# Program to calculate Fibonacci sequence

# The first function randomly generates the terms
import random


def is_fibonacci(n):
    """Formula =>  Fn = Fn-1 + Fn-2"""
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (is_fibonacci(n - 1) + is_fibonacci(n - 2))

print()
n_terms = random.randint(1, 100)
print(f"The terms randomly generated = {n_terms}")
print()
if n_terms <= 0:
    print("Fibonacci only works with positive numbers.")
else:
    print("Fibonacci sequence for terms entered: ")
    for i in range(0, n_terms):
        print(is_fibonacci(i))


# The second function uses terms from user input
def is_fibonacci(n):
    """Formula =>  Fn = Fn-1 + Fn-2"""
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (is_fibonacci(n - 1) + is_fibonacci(n - 2))

print()
n_terms = int(input("Enter terms: "))
print()
if n_terms <= 0:
    print("Enter a positive number.")
    n_terms = int(input("Try again. Enter terms: "))
    print()
print("Fibonacci sequence for terms entered: ")
for i in range(0, n_terms):
    print(is_fibonacci(i))
