# input string
user_input = input("Enter a string: ")
# intialize  to false
found_letter = False
is_all_upper = True

# loop character
for character in user_input:
#     if a letter is found, set to true, if lowercase, false
    if ("A" <= character <= "Z") or ("a" <= character <= "z"):
        found_letter = True
        if "a" <= character <= "z":
            is_all_upper = False
            break

# if one letter is found and no lowercase, print true, else false
if found_letter and is_all_upper:
    print(f"Result: {True}")
else:
    print(f"Result: {False}")