########################################################################################################
#                                 Exercise Prompt
######################################################################################################
#
## Goal: a product has the lot number "037-00901-00027", made of a country code
## (037), a product code (00901) and a batch number (00027). Split the lot number
## into its three parts and print each one with its label.
#
#######################################################################################################
################################# First Attempt #######################################################
#
# print("This program prints country, product, and batch information.")
#
# lotNumber = "037-00901-00027"
#
# print(
#    "Country code: " + str(lotNumber[:3]),
#    " Product code: " + str(lotNumber[4:9]),
#    " Batch number: " + str(lotNumber[10:]),
# )
#
######################################################################################################
#                                 My Corrected Code
#################################                   ##################################################
#  Problem with initial code: initial code did not match exact output format, unneeded str(),
#  breaks if the lot number ever changes format, and no validation of the lot number.
#  What I've learned in this exercise rework:
#   - split: cuts a string into a list at a separator, so lengths don't matter.
#   - len() and in/not in: count a list's items and search it.
#   - Validate after splitting: the right number of parts doesn't mean every part is filled in.
#   - .strip() on each piece: a string of spaces is not empty until you strip it.
#   - Building a cleaned list: start with [], loop, and .append().
#   - Simpler conditions: "" in codes already gives True or False, so == True isn't needed.

print("This program prints country, product, and batch information.")

required_format = "000-00000-00000"
lot_number = "037-00901-00027"
codes = lot_number.split("-")
clean_codes = []

for part in codes:
    clean_codes.append(part.strip())

if len(clean_codes) != 3:
    print(f"Invalid Lot Number. Expected format: {required_format}")
elif "" in clean_codes:
    print(f"Invalid Lot Number - empty part. Expected format: {required_format}")
else:
    print(
        f"Country code: {clean_codes[0]}, Product code: {clean_codes[1]}, Batch number: {clean_codes[2]}."
    )
