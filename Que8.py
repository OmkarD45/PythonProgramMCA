'''
Write a python program to use following , methods of string: isdigit(), 
capitalize(), casefold(), encode(), isidentifier(), 
'''
# Input string
input_string = input("Enter a string: ")

# isdigit() method
if input_string.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

# capitalize() method
capitalized_string = input_string.capitalize()
print("Capitalized string:", capitalized_string)

# casefold() method
casefolded_string = input_string.casefold()
print("Casefolded string:", casefolded_string)

# encode() method
encoded_string = input_string.encode()
print("Encoded string:", encoded_string)

# isidentifier() method
if input_string.isidentifier():
    print("The string is a valid identifier.")
else:
    print("The string is not a valid identifier.")
