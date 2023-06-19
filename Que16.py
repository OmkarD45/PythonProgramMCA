'''
16. Write a program to print following pattern (Make program dynamic, take length and breadth from user)
 * * * * 
 *     * 
 *     *
 *     * 
 * * * *
'''
def print_pattern(length, breadth):
    for i in range(length):
        for j in range(breadth):
            if i == 0 or i == length - 1 or j == 0 or j == breadth - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Take input from the user for length and breadth
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

# Call the function to print the pattern
print_pattern(length, breadth)