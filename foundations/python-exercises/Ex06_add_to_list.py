#######################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: start with a list of names, ask the user for their name, add it to the
## end of the list, and print the updated list.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This progam adds your name to a guest register.")
# names = ["Amy", "Cory", "Charles", "Frankie", "Georgina", "Kimberly", "Joe"]
#
# newName = input("Please enter your first name: ")
# names.append(newName)
#
# print("You entered: ", newName)
# print("The list of guests is: ", names)
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - No check for empty or spaces-only names.
#    - It printed the list with brackets and quotes.
#    - Only a first name was collected, so duplicates were hard to tell apart.
#    - No capitalization or consistent format.
#  What I've learned in this exercise rework:
#    - append: adds an item to the end of a list.
#    - ", ".join(list): turns a list of strings into one readable string.
#    - Reuse a function: ask_name from Ex02 handled both the first and last name.
#    - try is only for code that can raise an error: nothing here can, so I didn't use one. A bare try adds clutter.
#    - Names are hard to capitalize: .capitalize() lowercases the rest of a name, so McDonald becomes Mcdonald. Uppercasing only the first letter (name[0].upper() + name[1:]) keeps what the user typed.
#    - Check for empty before [0]: ""[0] raises an error.
#    - Messages must match behavior: the confirmation prompt had its logic reversed, so a test run caught what reading the code didn't.
#
print("This program adds your name to a guest register.")

guest_list = [
    "Amy C.",
    "Cory B.",
    "Charles G.",
    "Frankie M.",
    "Georgina A.",
    "Kimberly B.",
    "Joe G.",
]


def ask_name(prompt):
    while True:
        new_register = input(prompt)
        cleaned_nr = new_register.strip()
        if cleaned_nr == "":
            print("Name can't be empty.")
        else:
            print(f'You entered "{new_register}"')
            print("Press 'Enter' to accept")
            print(
                "Press any letter or number followed by 'Enter' to re-enter your name"
            )
            name_check = input(": ")
            second_chance = name_check.strip()
            if second_chance == "":
                return cleaned_nr[0].upper() + cleaned_nr[1:]


first_name = ask_name("Please enter your first name: ")
last_name = ask_name("Please enter your last name: ")

new_guest = f"{first_name} {last_name[0]}."
guest_list.append(new_guest)

print(", ".join(guest_list))
