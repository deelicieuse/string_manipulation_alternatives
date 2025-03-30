# prompt for string
user_input = input("Enter a string: ")
index = len(user_input) - 1 # set to last character of the string

# while non-negative and character at index is a space, decrement index
while index >= 0 and user_input[index] == " ":
    index -= 1

# slice the string from start and store in result
# print result