user_input = input("Enter a string: ") # prompt for string and width
width = int(input("Enter total width: "))
num_spaces = width - len(user_input) # calculate needed spaces as width minus string length
# if spaces needed is positive, set spaces to string
# print result