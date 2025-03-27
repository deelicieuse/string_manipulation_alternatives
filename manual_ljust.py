# prompt string and width
user_input = input("Enter a string: ")
desired_width = int(input("Enter width: "))

# if length of string is less than width, calculate spaces
if len(user_input) < desired_width:
    result = user_input + " " * (desired_width - len(user_input))

# else keep string
# print result
