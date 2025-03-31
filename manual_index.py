user_input = input("Enter a string: ") # prompt for string and substring to find
sub_str = input("Enter substring to find: ")
sub_len = len(sub_str)
found = False
for i in range(len(user_input) - sub_len + 1): # loop over each starting index in the string, check for match
# if a match is found, print index and break
# if no match is found, print "Not found"