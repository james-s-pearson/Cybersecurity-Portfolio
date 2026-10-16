############################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: a color-guessing game. Each round, pick a random color from a list and let
## the player keep guessing until they get it. Then ask whether to play again, and
## keep going until the player answers "no".
#
#######################################################################################################
################################# First Attempt #######################################################
#
#
# print("This is a game that requires a user to guess a color randomly selected by the system. You can play until you are tired.")
#
# import random
#
# colors = ["black", "blue", "green", "yellow", "purple", "red", "white", "brown", "orange"]
#
# response = "yes"
# playAgain = "yes"
#
# while True:
#     if response == playAgain:
#         answer = colors[random.randint(0,8)]
#         guess = input("Please guess a color: ").lower()
#         while True:
#             if guess == answer:
#                 break
#             else:
#                 guess = input("Guess again: ")
#         print("You guessed it!")
#         response = input("Would you like to play again? Type 'Yes' or 'No': ").lower()
#     else:
#         break
# print("Thank you for playing. ")
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - The retry prompt (guess = input("Guess again: ")) skipped .lower(), so the same word could pass on the first try and fail on the second.
#    - Each prompt was written twice, so the clean-up steps drifted apart.
#    - Answers to "play again?" were never validated, so any other word quietly ended or continued the game.
#    - The color list printed with brackets and quotes.
#    - The outer loop depended on two starter variables that had to match each other.
#  What I've learned in this exercise rework:
#    - One input() per prompt: put the prompt inside a while True loop, so .lower() and .strip() exist in exactly one place.
#    - Duplication causes drift: the bug in the retry prompt appeared because the same line existed twice and only one copy was updated.
#    - ", ".join(list): it prints a list as readable text.
#    - Act on an answer where you get it: the old design stored the answer in a "note" variable for the top of the loop to read.
#       + Checking it right away removed the note, the starter values and the if/else wrapper.
#    - Starter variables are a sign: if a variable exists only to satisfy a test the first time through, the loop can probably be restructured.
#    - in: x in ("yes", "no") replaces a chain of == and or, and is easier to extend.
#    - Print debugging: a temporary print before each break shows which exit ran.
#       + It also proved the old else was dead code.

import random

print(
    "This is a game that requires a user to guess a color randomly selected by the system."
)
print("You can play until you are tired.")
print(
    "***************************************************************************************"
)

colors = [
    "black",
    "blue",
    "green",
    "yellow",
    "purple",
    "red",
    "white",
    "brown",
    "orange",
]

while True:
    secret_color = random.choice(colors)
    print("I'm thinking of one of the following colors:")
    print(", ".join(colors))
    print("Can you guess the color I'm thinking?")
    print("****************************************************")
    while True:
        guess = input("Type your guess here: ").lower()
        clean_guess = guess.strip()
        if clean_guess == secret_color:
            break
        else:
            print("Wrong answer. Try again")
    print(f"You guessed it! The color was {secret_color}")
    while True:
        keep_playing = input(
            "Would you like to play again? Type 'Yes' or 'No': "
        ).lower()
        clean_keep_playing = keep_playing.strip()
        if clean_keep_playing in ("yes", "no"):
            break
        else:
            print(
                'Invalid Input. You must submit "Yes" to keep playing, or "No" to quit.'
            )
    if clean_keep_playing == "no":
        break
print("Thank you for playing!")
