# prompt for string and suffix
user_input = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
suffix_len = len(suffix) # calculate length of suffix
# if the substring at the end matches suffix, remove it
if suffix_len <= len(user_input) and user_input[-suffix_len:] == suffix:
    result = user_input[:-suffix_len]

# else, keep the string
# print result