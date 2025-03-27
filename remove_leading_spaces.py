# prompt input
user_input = input("Enter a string: ")

# intialize index to zero
index = 0

# loop until a non-space character is found
while index < len(user_input) and user_input[index] == " ":
    index += 1
result = user_input[index:]

# print result
