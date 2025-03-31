user_input = input("Enter a string: ") # prompt for string and substring
sub_str = input("Enter substring to find from the right: ")
sub_len = len(sub_str)
found = False
# loop over each index start in the string, check for a match
# if  match found, print index and break
# else, print "Not Found"