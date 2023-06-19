'''
Write a python program which finds the maximum number from num1 to 
num2 (num2 inclusive) based on the following rules.
1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). 
Populate the number into a list, if the below conditions are satisfied
 a. Sum of the digits of the number is a multiple of 3
 b. Number has only two digits
 c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
'''
def calculate_max_number(num1, num2):
    if num1 >= num2:
        return -1

    numbers = []

    for num in range(num1, num2 + 1):
        if sum_of_digits(num) % 3 == 0 and is_two_digit_number(num) and num % 5 == 0:
            numbers.append(num)

    if not numbers:
        return -1

    return max(numbers)


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def is_two_digit_number(number):
    return 10 <= number <= 99


# Example usage:
num1 = 12
num2 = 23

result = calculate_max_number(num1, num2)
print("Maximum number:", result)
