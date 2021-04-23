#!/usr/bin/python3
# program to ascertain if user input is leap year

print()
print("Enter any year to find out if it's a leap year or not")
year_input = int(input("Please enter any year: "))
print(f"You have chosen {year_input}. Checking ...")
print()

ans = ['YES', 'Y', 'yes', 'y']
ans_1 = ans
while ans_1 == ans:
    if len(str(year_input)) == 4:
        if (year_input % 4) == 0:
            if (year_input % 100) == 0:
                if (year_input % 400) == 0:
                    print(True)
                else:
                    print(False)
            else:
                print(True)
        else:
            print(False)
    else:
        print("That's not a correct year format.")

    print()
    ques = input("Do you want to try again? ")

    if ques not in ans:
        exit(0)
    else:
        year_input = int(input("Please enter any year: "))
        print(f"You have chosen {year_input}. Checking ...")
        print()
