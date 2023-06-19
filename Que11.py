'''
Que.11 Write a python program to solve following problem statement:You have x 
no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an 
item for amount z. The shopkeeper wants you to provide exact change. You 
want to pay using minimum number of coins. How many 5 rupee coins and 
1 rupee coins will you use? If exact change is not possible then display -1
'''
def calculate_change(x, y, z):
    # Check if exact change is possible
    if z > (x * 5 + y):
        return -1

    # Calculate the number of 5 rupee coins required
    num_5_rupee_coins = min(x, z // 5)

    # Calculate the remaining amount
    remaining_amount = z - (num_5_rupee_coins * 5)

    # Calculate the number of 1 rupee coins required
    num_1_rupee_coins = min(y, remaining_amount)

    return num_5_rupee_coins, num_1_rupee_coins


# Take input from the user for the number of 5 rupee coins, number of 1 rupee coins, and the amount to be paid
x = int(input("Enter the number of 5 rupee coins: "))
y = int(input("Enter the number of 1 rupee coins: "))
z = int(input("Enter the amount to be paid: "))

# Call the calculate_change function to calculate the minimum number of coins required
change = calculate_change(x, y, z)

# Display the result
if change == -1:
    print("-1")
else:
    num_5_rupee_coins, num_1_rupee_coins = change
    print("Minimum number of coins required: ")
    print("5 rupee coins:", num_5_rupee_coins)
    print("1 rupee coins:", num_1_rupee_coins)
