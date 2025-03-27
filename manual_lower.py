# input string
user_input = input("Enter a string: ")

# initialize empty string
result = ""

# for each uppercase, convert to lowercase else keep
for character in user_input:
    if "A" <= character <= "Z":
        result += chr(ord(character) + 32)
    else:
        result += character

# print result
print(f"Result: {result}")