# prompt string and prefix
user_input = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

# calculate length of prefix
prefix_length = len(prefix)

# check if beginning of string matches prefix
if user_input[:prefix_length] == prefix:
#     if yes, remove, else, keep
    result = user_input[:prefix_length]
else:
    result = user_input


# print result