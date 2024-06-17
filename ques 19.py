import string

def remove_punctuation(input_string):
    
    translator = str.maketrans('', '', string.punctuation)
    
    
    no_punctuation_string = input_string.translate(translator)
    
    return no_punctuation_string


user_input = input("Enter a string: ")

cleaned_string = remove_punctuation(user_input)

# Print the cleaned string
print("\nString without punctuation:")
print(cleaned_string)