'''
A traveler on a visit to India is in need of some Indian Rupees (INR) 
but he has money belonging to another currency.
He wants to know how much money he should provide in the 
currency he has, to get the specified amount in INR.
Write a python program to implement a currency calculator which 
accepts the amount needed in INR and the name of the currency 
which the traveler has. The program should identify and display the 
amount the traveler should provide in the currency he has, to get the 
specified amount in INR.
Note: Use the forex information provided in the table below for the 
calculation. Consider that only the currency names mentioned in the 
table are valid. For any invalid currency name, display -1.
Currency Equivalent of 1.00 INR
Euro 0.01417
British Pound 0.0100
Australian Dollar 0.02140
Canadian Dollar 0.02027
(Note : You have to use Class and functions , exception handling 
concepts)
'''
class CurrencyCalculator:
    def __init__(self):
        self.conversion_rates = {
            "Euro": 0.01417,
            "British Pound": 0.0100,
            "Australian Dollar": 0.02140,
            "Canadian Dollar": 0.02027
        }

    def convert_currency(self, amount_inr, currency):
        try:
            conversion_rate = self.conversion_rates[currency]
            amount_foreign_currency = amount_inr / conversion_rate
            return round(amount_foreign_currency, 2)
        except KeyError:
            return -1


# Create an instance of the CurrencyCalculator class
calculator = CurrencyCalculator()

# Take input from the user for the amount in INR and the currency name
amount_inr = float(input("Enter the amount needed in INR: "))
currency = input("Enter the name of the currency you have (Euro/British Pound/Australian Dollar/Canadian Dollar): ")

# Call the convert_currency method to get the equivalent amount in the traveler's currency
amount_foreign_currency = calculator.convert_currency(amount_inr, currency)

# Check if the returned value is valid or not
if amount_foreign_currency == -1:
    print("Invalid currency name. Please enter a valid currency.")
else:
    print("Amount to provide in", currency + ":", amount_foreign_currency)
