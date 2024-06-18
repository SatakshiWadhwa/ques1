def find_max_min(numbers):
    if not numbers:
        return None, None  # If the list is empty, return None for both max and min
    
    max_value = numbers[0]
    min_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value


numbers = [ 1 , 2, 3, 50, 30, 20, 60, 10]
max_value, min_value = find_max_min(numbers)
print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")












