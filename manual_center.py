# prompt string and width
user_input = input("Enter a string: ")
desired_width = int(input("Enter width: "))

# if length of string < width, calculater space
if len(user_input) < desired_width:
    total_padding = desired_width - len(user_input)
    left_padding = total_padding // 2 # and split string into left and right
    right_padding = total_padding - left_padding
    result = " " * left_padding + user_input + " " * right_padding
else: # else keep string as is
    result = user_input

# print result