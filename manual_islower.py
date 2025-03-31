user_input = input("Enter a string: ") # prompt for string
found_letter = False # set flags
all_lower = True
for char in user_input: # for each character,
    if ("a" <= char <= "z") or ("A" <= char <= "Z"):     # if letter then mark found_letter
        found_letter = True
        if not ("a" <= char <= "z"): # if not lowercase, set all_lower to false and break
            all_lower = False
            break
print(f"Result: {all_lower if found_letter else False}") # print result (true if all letters are lowercase and at least one letter exists, else false)
