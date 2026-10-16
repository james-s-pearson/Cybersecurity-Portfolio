##########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: ask for a height in inches and a weight in pounds, calculate the BMI with
## BMI = (weight / (height x height)) x 703, then print the BMI and its category:
## below 18.5 is underweight, 18.5 to 24.9 is normal weight, above 24.9 and below 30
## is overweight, and 30 or above is obesity.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This program calculates the user's BMI(body mass index) and prints the BMI along with the categorization.")
#
# height = float(input("Please enter your height in inches: "))
# weight = float(input("Please enter your weight in pounds: "))
#
# bmi = round(float((weight / (height * height)) * 703),1)
#
# if(bmi <= 18.5):
#     print("Your BMI is:", bmi, "and you are underweight.")
# elif(bmi > 18.5 and bmi <= 24.9):
#     print("Your BMI is:", bmi, "and you are normal weight.")
# elif(bmi > 24.9 and bmi <= 29.9):
#     print("Your BMI is:", bmi, "and you are overweight.")
# else:
#     print("Your BMI is:", bmi, "and you are obesity.")
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - No validation: text crashed it, and 0, negatives, nan and inf were accepted. A height of 0 raised a division error.
#    - The BMI was rounded to 1 decimal inside the formula.
#    - The last else had the grammar "you are obesity".
#    - Four repeated print lines, each with its own formatting.
#    - It classified one number and could display a different one.
#  What I've learned in this exercise rework:
#    - Use a function: ask_measurement takes the prompt and handles both weight and height.
#    - Validate before using: <= 0 and not math.isfinite() catch zero, negatives, nan and inf before they reach a division.
#    - Round once: round the BMI one time, then use that same number for the display and the classification, so the screen can't disagree with itself.
#    - Boundaries need a decision: < versus <= changes which category exactly 18.5 lands in.
#    - An elif chain removes redundant tests: each elif already knows the earlier conditions failed, so and bmi > 18.5 was unnecessary.
#    - Deliberate choices: chose not to add upper limits, and kept four print lines.

import math

print(
    "This program calculates the user's BMI(body mass index) and prints the BMI along with the categorization."
)


def ask_measurement(prompt):
    while True:
        try:
            measurement = float(input(prompt))
            if measurement <= 0 or not math.isfinite(measurement):
                print("Invalid Submission. Must be a positive real number.")
            else:
                return measurement
        except ValueError:
            print("Invalid Input. Please use only numbers and decimals.")


weight = ask_measurement("Type your weight in pounds (ex. 175.5): ")
height = ask_measurement("Type your height in inches (ex. 65.5): ")

bmi = round(((weight / (height * height)) * 703), 2)
if bmi < 18.5:
    print(f"Your BMI is: {bmi} and you are underweight.")
elif bmi <= 24.9:
    print(f"Your BMI is: {bmi} and you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is: {bmi} and you are overweight.")
else:
    print(f"Your BMI is: {bmi} and you are obese.")
