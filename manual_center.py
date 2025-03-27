# prompt string and width
user_input = input("Enter a string: ")
desired_width = int(input("Enter width: "))

# if length of string < width, calculater space
if len(user_input) < desired_width:
    total_padding = desired_width - len(user_input)
# and split string into left and right
# else keep string as is
# print result