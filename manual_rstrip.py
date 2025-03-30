# prompt for string
user_input = input("Enter a string: ")

# set to last character of the string
index = len(user_input) - 1

# while non-negative and character at index is a space, decrement index
# slice the string from start and store in result
# print result