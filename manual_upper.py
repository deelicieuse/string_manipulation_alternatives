user_input = input("Enter a string: ") # prompt for string
result = "" # initialize empty result
for char in user_input: # for each character,
    if "a" <= char <= "z": # if lowercase, convert to uppercase
        result += chr(ord(char) - 32)
    else: # else, add character
        result += char
# print result