########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: ask for a circle's radius, then calculate and print its area (pi x r
## squared) and its circumference (2 x pi x r).
#
#######################################################################################################
################################# First Attempt #######################################################
#
# import math
#
# print("This program calculates the area and circumference or a circle.")
#
# radius = input("What is the radius of the circle you would like to measure? ")
# area = 3.14 * (float(radius) ** 2)
# circumference = round(float(2 * 3.14 * (float(radius))), 3)
#
# print("The radius you entered was ", radius)
# print("The area is: ", area)
# print("The circumference is: ", circumference)
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code: was not using the import math lib for calculations, lacked
#  input validation, and results printed with inconsistent rounding.
#  What I've learned in this exercise rework:
#   - math.pi: it's more precise than a typed 3.14.
#   - float() accepts nan and inf: every comparison with nan is False, so <= 0 can't catch it.
#   - math.isfinite() returns a bool, not the number. Use it as a test in the if, never in the assignment.
#   - Round once, and don't also format when the value is only displayed.
#   - :g: it's fine for the radius, but it can switch large results to scientific notation.
#   - Constants: a value that shouldn't change gets a capitalized name, like MAX_RADIUS.

import math

print("This program calculates the area and circumference of a circle.")

MAX_RADIUS = 1e150
radius = 0.0
valid_input = False
while not valid_input:
    try:
        radius = float(
            input("What is the radius of the circle you would like to measure? \n:")
        )
        if radius <= 0 or not math.isfinite(radius):
            print(
                "Invalid number. Radius must be a number greater than zero but less than infinity."
            )
        elif radius >= MAX_RADIUS:
            print(f"Invalid number. Radius must be smaller than {MAX_RADIUS}.")
        else:
            valid_input = True
    except ValueError:
        print("Invalid entry. Only use numbers and decimal points.")

area = round(math.pi * (radius**2), 2)
circumference = round(2 * math.pi * radius, 2)

print(f"The radius you entered was {radius:g}")
print(f"The area is: {area}")
print(f"The circumference is: {circumference}")
