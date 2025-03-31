user_input = input("Enter a string: ") # prompt for string and width
width = int(input("Enter total width: "))
num_zeros = width - len(user_input) # calculate zeros as width minus string length
# if zeros needed is positive, add zeros to string
# else, set string to result
# print result