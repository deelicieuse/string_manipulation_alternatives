# prompt for string
user_input = input("Enter a string: ")

# if string is not empty, capitalize first character
if user_input:
    first_character = user_input[0]
    rest_of_string = user_input[1:]
    if "a" <= first_character <= "z":
        first_character = chr(ord(first_character) - 32)
    rest_of_string_lower = "" # and convert remaining characters to lower case
    for char in rest_of_string:
        if "A" <= char <= "Z":
            rest_of_string_lower += chr(ord(char) + 32)
    result = first_character + rest_of_string_lower
# else, set as empty string
# print result