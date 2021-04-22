#!usr/bin/python3
# Binary Search Algorithm
# Fetch a number(user input) from a randomly generated list using binary search


import numpy as np

numList = np.arange(1, 100, 2)
# print(numList)
print()
print("Let's check if the number you'll choose is in the number list")
num = int(input("Please enter a number between 1 and 100: "))
print()


def binary_search(arrList, n):
    # search for a number using binary search algorithm
    start = 0
    end = len(arrList) - 1
    while (start <= end):
        midpoint = (start + end) // 2
        if (arrList[midpoint] > n):
            end = midpoint - 1
        elif (arrList[midpoint] < n):
            start = midpoint + 1
        else:
            return midpoint
    return None

result = binary_search(numList, num)
if result is None:
    print("The number chosen is not in the list.")
else:
    print(f"The number chosen is at index {result}")
