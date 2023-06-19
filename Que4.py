'''
Write a Python program that creates two threads to find and print even and 
odd numbers from 30 to 50
'''
import threading

# Function to print even numbers
def print_even():
    for num in range(30, 51):
        if num % 2 == 0:
            print("Even number:", num)

# Function to print odd numbers
def print_odd():
    for num in range(30, 51):
        if num % 2 != 0:
            print("Odd number:", num)

# Create two threads for even and odd numbers
t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

print("Done")
