user_input = input("Enter a string: ") # prompt for string and width
width = int(input("Enter total width: "))
num_spaces = width - len(user_input) # calculate needed spaces as width minus string length
if num_spaces > 0: # if spaces needed is positive, add spaces to string
    result = " " * num_spaces + user_input
else:
    result = user_input
print(f"Result: {result}") # print result