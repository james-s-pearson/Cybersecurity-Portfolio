######################################################################################################
#                           Exercise Prompt
######################################################################################################
#
## Goal: ask for a first, middle and last name, then print the person's initials
## in a sentence ("Your initials are ___").
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This program tells you your initials.")
#
# firstName = input("Please enter your First Name: ")
# middleName = input("Please enter your Middle Name: ")
# lastName = input("Please enter your Last Name: ")
#
# print("Your initials are: " + str(firstName[:1]) + str(middleName[:1]) + str(lastName[:1]))
#
#######################################################################################################
#                                 My Corrected Code
#################################                   ###################################################
#  Problem with initial code: the initial program crashes on an empty middle name and can be improved
#  What I've learned in this exercise rework:
#    - Indexing vs. slicing: ""[0] raises an error, while ""[:1] returns "".
#    - Truthiness: an empty string counts as false in an if.
#    - Functions: a parameter for what changes, and return to hand the answer back.
#    - Linter warnings: a function with no return on some path gives back None.

print("This program tells you your initials.")


def ask_name(prompt):
    while True:
        name = input(prompt)
        cleaned_name = name.strip()
        if cleaned_name == "":
            print("********************************************************")
            print("Please enter a valid Name")
            print("********************************************************")
        else:
            return cleaned_name


f_name = ask_name("Please enter your First Name: ")

cleaned_middle_name = ""
valid_input = False
while not valid_input:
    middle_name = input("Please enter your Middle Name: ")
    cleaned_middle_name = middle_name.strip()
    if cleaned_middle_name == "":
        print(
            "************************************************************************"
        )
        print("Press 'Enter' to leave Middle Name blank")
        print("Press any letter or number followed by 'Enter' to re-enter Middle Name")
        mn_check = input(": ")
        cleaned_mn_check = mn_check.strip()
        print(
            "************************************************************************"
        )
        if cleaned_mn_check == "":
            break
    else:
        valid_input = True

l_name = ask_name("Please enter your Last Name: ")

print(
    f"Your initials are {f_name[:1].capitalize()}{cleaned_middle_name[:1].capitalize()}{l_name[:1].capitalize()}."
)
