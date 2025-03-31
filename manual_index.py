user_input = input("Enter a string: ") # prompt for string and substring
sub_str = input("Enter substring to find from the right: ")
sub_len = len(sub_str)
found = False
for num in range(len(user_input) - sub_len, -1, -1): # loop over each index start in the string, check for a match
    if user_input[num:num + sub_len] == sub_str: # if  match found, print index and break
        print(f"Result: {num}")
        found = True
        break
if not found: # if not, print "Not Found"
    print("Result: Not found")