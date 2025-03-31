user_input = input("Enter a string: ") # prompt for string and prefix
prefix = input("Enter prefix: ")
prefix_len = len(prefix) # calculate length of prefix
if user_input[:prefix_len] == prefix: # compare extracted substring with prefix
    print("Result: True") # print true if they match
else:
    print("Result: False") # else print false
