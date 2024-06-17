def to_title_case(input_string):
    # Convert the string to title case
    title_cased_string = input_string.title()
    return title_cased_string

# Ask the user to input a string
user_input = input("Enter a string: ")

# Convert the string to title case
title_cased = to_title_case(user_input)

# Print the title-cased string
print("\nTitle-cased string:")
print(title_cased)