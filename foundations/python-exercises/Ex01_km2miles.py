######################################################################################################
#                           Exercise Prompt
######################################################################################################
#
## Goal: ask for a distance in kilometres, convert it to miles, and print the result.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This program convers Kilometers to Miles.")
#
# km = float(input("Please enter the number of Kilometers: "))
# miles = float(km / 1.609344)
#
# print(km, "km =", round(miles, 2), "Miles.")
#
######################################################################################################
#                                My Corrected Code
################################                   ###################################################
#  Problem with initial code: the initial code crashed upon receiving "bad" input from users.
#  What I've learned in this exercise rework:
#   - try/except only protects the code indented under it, so the risky line has to go inside the try block.
#   - A while loop plus try/except keeps asking until the user types something valid.
#   - = stores a value and == compares two values.
#   - f-strings put variables right into your text, e.g. f"{name}".
#   - Format codes: .2f means 2 decimal places, .2g means 2 digits in total, and plain g drops a trailing .0.
#   - Linter warnings: a warning can point to something real, even when the code runs fine.


print("This program converts Kilometers to Miles.")

valid_number = False
km = 0.0  # silences linting error that km may be unbounded
while not valid_number:
    try:  # use a try block to handle errors to prevent program from crashing from undesired user input
        km = float(
            input("Please enter the number of Kilometers: ")
        )  # needs to be in the try block
        if km <= 0:
            print("Invalid. Please enter a number greater than 0.")
        else:
            valid_number = True
    except (
        ValueError
    ):  # added "ValueError" to overcome linting error for using bare except
        print("Invalid. Only use numbers and decimal points.")

miles = km / 1.609344

print(
    f"{km:g} Kilometers = {miles:.2f} Miles."
)  # using f-string allows output to be piped into a variable for broader use cases
