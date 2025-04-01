user_input = input("Enter a string: ") # prompt for string and width
width = int(input("Enter total width: "))
num_zeros = width - len(user_input) # calculate zeros as width minus string length
if num_zeros > 0: # if zeros needed is positive,
    result = "0" * num_zeros + user_input  # add zeros to string
else: # else, set string to result
    result = user_input
print(f"Result: {result}")# print result