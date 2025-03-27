# prompt for string
user_input = input("Enter a string: ")

# if string is not empty, capitalize first character
if user_input:
    first_character = user_input[0]
    rest_of_string = user_input[1:]
    if "a" <= first_character <= "z":
        first_character = chr(ord(first_character) - 32)

# and convert remaining characters to lower case
# else, set as empty string
# print result