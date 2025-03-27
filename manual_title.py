# prompt for string
user_input = input("Enter a string: ")
words = user_input.split() # split string into words
result = ""

# for each word
for word in words:
    if word:
        first_character = word[0]
        rest_of_word = word[1:]
#     capitalize first character
#     convert remaiing character to lower case
# combine and print result
