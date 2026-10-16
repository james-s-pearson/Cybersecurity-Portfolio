###########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: ask the user for 8 names, store them in a list, then pick one at random
## and print it.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# import random
#
# print("This program asks the user to input 8 names, and then prints a random name from the list.")
#
# names = []
#
# while len(names) < 8:
#     people = input("Please enter a name: ")
#     names.append(people)
#
# print(names[random.randint(0,7)])
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code:
#    - Blank or spaces-only names were accepted.
#    - 8 and 7 were written separately and had to match by hand.
#    - people held a single name, which misled the reader.
#    - The output had no explanation.
#    - It gave the user no sense of progress.
#  What I've learned in this exercise rework:
#    - One number, one place: desired_length feeds the message, the loop and the counter.
#       + It also made testing quick, because one edit switches between 8 and 3.
#    - A loop condition that reads the list: while len(people) < desired_length doesn't count a rejected name
#       + So the counter len(people) + 1 stays correct without a separate variable.
#    - random.choice(list): it picks an item directly, so no index has to match the list length.
#    - Validate before appending: strip, check for empty, confirm, and only then add.
#    - The user is the authority on their own name: capitalization can't be fixed reliably.
#    - Show what will be stored: the confirmation prompt echoes clean_person, so the user approves the real value.
#    - Don't over-validate names: I chose not to restrict characters, because names vary.
#    - Choices to record: the confirm step is extra work beyond the assignment, added on purpose.

import random

desired_length = 8
people = []

print(
    f"This program asks the user to input {desired_length} names, and then prints a random name from the list."
)

while len(people) < desired_length:
    person = input(f"Please enter name {len(people) + 1} to add to the list: ")
    clean_person = person.strip()
    if clean_person == "":
        print("Name can't be empty.")
    else:
        print(f'Do you want to add "{clean_person}" to the list?')
        print("Press 'Enter' to accept")
        print("Press any letter or number followed by 'Enter' to re-type the name")
        name_check = input(": ")
        second_chance = name_check.strip()
        if second_chance == "":
            people.append(clean_person)

random_person = random.choice(people)
print(f"Picking a random name: {random_person}")
