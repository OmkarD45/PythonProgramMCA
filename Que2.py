'''
Write a Python program to calculate the factorial of a number using 
multiple threads.

'''
import threading

# Function to calculate the factorial of a number
def calculate_factorial(num, result):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    result[num] = fact

# Function to create threads and calculate factorial
def calculate_factorial_with_threads(num):
    # Dictionary to store the results
    result = {}

    # Create a list to hold the threads
    threads = []

    # Create a thread for each subtask
    for i in range(1, num + 1):
        t = threading.Thread(target=calculate_factorial, args=(i, result))
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for the threads to finish
    for t in threads:
        t.join()

    # Print the factorial results
    for i in range(1, num + 1):
        print(f"Factorial of {i}: {result[i]}")

# Take input from the user
num = int(input("Enter a number: "))

# Calculate factorial using multiple threads
calculate_factorial_with_threads(num)
