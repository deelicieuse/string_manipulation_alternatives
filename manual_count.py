user_input = input("Enter a string: ")# prompt for string and substring to count
sub_str = input("Enter substring to count: ")
count = 0 # initialize count to 0
sub_len = len(sub_str)
for i in range(len(user_input) - sub_len + 1): # loop over each start of string, check if substring matches
    if user_input[i:i + sub_len] == sub_str:
        count += 1 # add count if match found
# print count