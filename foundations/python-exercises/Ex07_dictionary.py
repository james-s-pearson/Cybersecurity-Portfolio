########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: build a dictionary describing one person (name, gender, age, address and
## phone). Ask which detail the user wants, then print that value, or a message if
## the detail does not exist.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# sango = {
#     "name": "Sango Miller",
#     "age": "4",
#     "birthday": "05-21-2025",
#     "breed": "Cane Corso",
#     "color": "Brindle",
#     "gender": "male",
#     "vacination status": "current",
# }
#
# print("This program allows the user to request information about my dog.")
#
# query = input("What would you like to know about my dog? ",)
#
# print("You requested to know my dog's", '"' + query + '"')
# print(sango.get(query, "Information not found."))
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
##  Problem with initial code:
#    - The dictionary didn't include all the assignment's fields (address, phone).
#    - The stored age was a fixed value that could go out of date, and it contradicted the birthday.
#    - Case and spaces made valid queries fail.
#    - The user wasn't told which keys existed.
#    - Typo in a key name.
##  What I've learned in this exercise rework:
#    - Dictionaries: keys map to values, and .get(key, default) returns the default instead of raising an error.
#    - .keys() and ", ".join(...): list the available keys for the user.
#    - Calculate, don't store: an age derived from the birthday can't go stale.
#    - One source of truth: write a value once and derive the rest, like the birthday with strptime and strftime.
#    - Named constants: ONE_YEAR explains itself in a way a bare number can't.
#    - .strip().lower(): normalize what the user types before looking it up.
#    - Nested quotes in f-strings: use different quote types inside, so the code runs on older Python too.
#    - Naive vs. aware datetimes: a datetime with no timezone is "naive". For a local script that only uses dates, that's fine.
#    - noqa: DTZ... records a deliberate choice instead of hiding a warning.
#    - time vs. datetime: time counts seconds (for timing and sleeping); datetime handles calendar dates and formatting.
#    - Subtracting datetimes gives a timedelta: use .days or .total_seconds() to get a plain number.
#    - Both sides of an operation must be the same type: datetime - float raised a TypeError. The error message tells the types on each side.
#    - Change one thing at a time: when several errors appear together, a single mismatch is often the cause.

from datetime import datetime

sango = {
    "name": "Sango Miller",
    "age": "",
    "birthday": "",
    "breed": "Cane Corso",
    "color": "Brindle",
    "gender": "male",
    "vaccination status": "current",
    "address": "123 Street, New York, NY",
    "phone": "555-444-3322",
}

sango_keys = ", ".join(sango.keys())
ONE_YEAR = 365
dob_string = "2025-05-21"
dob_format = "%Y-%m-%d"
dob_object = datetime.strptime(dob_string, dob_format)  # noqa: DTZ007
current_date = datetime.now()  # noqa: DTZ005
age = str(round(((current_date - dob_object).days) / ONE_YEAR, 1))
sango["age"] = age
sango["birthday"] = dob_object.strftime("%m-%d-%Y")

print("This program allows the user to request information about my dog.")
print(f"Available parameters are: {sango_keys}")
print(
    "******************************************************************************************"
)

while True:
    query = input("What would you like to know about my dog? ")
    clean_query = (query.strip()).lower()
    if clean_query == "":
        print("Invalid Input. Cannot submit a blank request.")
    else:
        break

print(f"You requested to know my dog's '{query}'.")
print(
    sango.get(
        clean_query, f"Information not found. \nAvailable parameters are: {sango_keys}"
    )
)
