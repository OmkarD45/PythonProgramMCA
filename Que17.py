'''
17. Write a program to print following pattern
 	    1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
'''
def print_pattern(n):
    for i in range(1, n+1):
        # Print spaces
        print("  " * (n-i), end="")
        
        # Print increasing sequence
        for j in range(1, i+1):
            print(j, end=" ")
        
        # Print decreasing sequence
        for j in range(i-1, 0, -1):
            print(j, end=" ")
        
        # Move to the next line
        print()

# Take input from the user for the number of rows in the pattern
n = int(input("Enter the number of rows: "))

# Call the function to print the pattern
print_pattern(n)
