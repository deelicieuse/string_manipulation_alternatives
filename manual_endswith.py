# prompt string and suffix
user_input = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# calculate length of suffix
suffix_length = len(suffix)

# if suffix is longer than string, print false
if suffix_length > len(input_str):
    print("Result: False")
elif suffix_length == 0: #     else compare end of string with suffix
    print("Result: True")
else: # print true if they match, else false
    if input_str[-suffix_length:] == suffix:
        print("Result: True")
    else:
        print("Result: False")


