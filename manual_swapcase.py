# prompt for string
user_input = input("Enter a string: ")
result = "" # initialize empty string

# for each character,
for character in user_input:
    if "a" <= character <= "z": #     if lowercase, convert to uppercase
        result += chr(ord(character) - 32)
#     if uppercase, convert to lowercase
#     else, keep string as is
# print result
