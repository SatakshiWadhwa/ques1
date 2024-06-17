def count_char_frequencies(input_string):
    # Create an empty dictionary to store character frequencies
    freq_dict = {}
    
    # Loop through each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in freq_dict:
            freq_dict[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            freq_dict[char] = 1
            
    return freq_dict

# Ask the user to input a string
user_input = input("Enter a string: ")

# Count character frequencies
frequencies = count_char_frequencies(user_input)

# Print the character frequencies
print("\nCharacter frequencies:")
for char, freq in frequencies.items():
    print(f"'{char}': {freq}")