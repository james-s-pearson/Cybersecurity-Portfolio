#########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: store my own age in a variable, ask the user for theirs, and print whether
## they are older than me, younger than me, or the same age.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This program asks your age, then compares it to my age and returns a result.")
#
# myAge = 37
# yourAge = float(input("Please enter your age in years: "))
#
# print("Your age is:", yourAge)
#
# if myAge > yourAge:
#     print("I am older than you.")
# elif myAge < yourAge:
#     print("You are older than me.")
# else:
#     print("We are the same age.")
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - It used float() for an age, which accepted 32.5, nan and inf.
#    - A letter crashed the program.
#    - Nothing stopped -5 or 500.
#    - myAge = 37 was typed in by hand, so it would go out of date on the next birthday.
#  What I've learned in this exercise rework:
#    - Whole numbers for ages: int() rejects 32.5, nan, inf and text, so a decimal or a letter can't slip through as an age.
#    - Calculate, don't store: an age comes from a birthday and a date, so it can't go out of date the way a typed 37 does.
#    - Compare (month, day) tuples: the year difference alone is wrong until the birthday arrives. The tuple comparison decides whether to subtract 1.
#    - A function takes a date and returns an age.
#    - Name parameters for what they hold: date tells a reader more than prompt did.
#    - Test both sides of a condition: today's date only exercised one branch. The day before, the day of and the day after the birthday proved the logic.
#    - One break after the whole if / elif / else chain: it replaces one in each branch, and runs only after a valid age has been compared.

from datetime import datetime

print("This program asks your age, then compares it to my age and returns a result.")

my_birthday = datetime(1990, 5, 13)  # noqa: DTZ001
current_date = datetime.now()  # noqa: DTZ005
# test = datetime(2026, 8, 23)


def age_calculator(date):
    age = date.year - my_birthday.year
    if (date.month, date.day) < (my_birthday.month, my_birthday.day):
        age = age - 1
    return age


my_age = age_calculator(current_date)
while True:
    try:
        user_age = int(input("Please enter your age in years: "))
        if 0 < user_age < 110:
            if user_age < my_age:
                print("You are younger than me.")
            elif user_age > my_age:
                print("You are older than me.")
            else:
                print("You are the same age as me.")
            break
        else:
            print("Invalid Input. Age must be greater than zero and less than 110.")
    except ValueError:
        print("Invalid Input. Letters and decimal numbers not supported.")
