
'''
Write a python program to find and display the product of three positive 
integer values based on the rule mentioned below:
It should display the product of the three values except when one of 
the integer value is 7. In that case, 7 should not be included in the 
product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. 
If no values can be included in the product, display -1.
'''
def calculate_product(a, b, c):
    if a == 7:
        return -1
    elif b == 7:
        return a
    elif c == 7:
        return a * b
    else:
        return a * b * c
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
product = calculate_product(a, b, c)

# Display the result
print("Product:", product)


