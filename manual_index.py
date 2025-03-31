user_input = input("Enter a string: ") # prompt for string and substring to find
sub_str = input("Enter substring to find: ")
sub_len = len(sub_str)
found = False
for num in range(len(user_input) - sub_len + 1): # loop over each starting index in the string, check for match
    if user_input[num:num + sub_len] == sub_str: # if a match is found, print index and break
        print(f"Result: {num}")
        found = True
        break
# if no match is found, print "Not found"