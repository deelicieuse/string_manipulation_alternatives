# prompt for string and suffix
user_input = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
suffix_len = len(suffix) # calculate length of suffix
# if the substring at the end matches suffix, remove it
# else, keep the string
# print result