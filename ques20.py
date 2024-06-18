def sum_of_numbers(numbers):
    return sum(numbers)


user_input = input("Enter a list of numbers, separated by spaces: ")


numbers_list = list(map(float, user_input.split()))


total_sum = sum_of_numbers(numbers_list)


print(f"\nThe sum of the numbers is: {total_sum}")