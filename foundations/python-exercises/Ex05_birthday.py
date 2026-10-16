#######################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: ask for a birthday written as DD-MM-YYYY, then print which month the
## person was born in, in a sentence such as "You were born in March."
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This is a program that takes your birth date in numbers and returns your birth month name.")
#
# dob = input("Please enter your birth date in DD-MM-YYYY format: ")
# month = (
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December",
# )
# answer = month[int(dob[3:5]) - 1]
#
#
# print("You entered: ", dob)
# print("You were born in ", answer)
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - Hard-coded character positions (dob[3:5]) broke with 5-3-1990.
#    - It crashed on text, a wrong separator, or a missing part.
#    - Month 0 silently gave December, because month[-1] is the last item.
#    - The output had extra spaces and no final period.
#  What I've learned in this exercise rework:
#    - split instead of positions: it works whatever the length of each part.
#    - int() handles leading zeros and spaces: int("03") and int(" 3 ") both work, so no extra stripping is needed.
#    - Negative indexes: month[-1] is the last item, so month 0 gave December silently, which is worse than a crash.
#    - Validate in order: split the parts first, convert them second, and check the range third.
#    - Reset a list at the start of each attempt: a list created outside the loop keeps old values across retries.
#    - One if/elif/else chain: starting a second if begins a new chain, so the else attached to the wrong one.
#    - Some mistakes can't be checked: a swapped day and month is still a valid date.
#       + You can either ask the user to confirm or state the format clearly.
#    - Test the edge cases: one-item inputs, too many parts, and text in one part.

print(
    "This is a program that takes your birth date in numbers and returns your birth month name."
)

expected_format = "DD-MM-YYYY"
month = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


while True:
    try:
        clean_dob = []
        dob = input(f"Enter your date of birth in {expected_format} format: ")
        dob_splits = dob.split("-")
        for part in dob_splits:
            clean_dob.append(int(part.strip()))
        if len(clean_dob) <= 2:
            print(f"Missing Input. \nExpected format is {expected_format}")
        elif len(clean_dob) >= 4:
            print(
                f"Additional submission detected. \nExpected format is {expected_format}"
            )
        elif clean_dob[1] <= 0 or clean_dob[1] >= 13:
            print("Invalid submission. Month must be between 1 and 12.")
        else:
            break
    except ValueError:
        print(f"Invalid submission. \nExpected format is {expected_format}")

print(f"You entered: {dob}")
print(f"You were born in {month[(clean_dob[1])-1]}.")
