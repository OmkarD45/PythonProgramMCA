'''

'''
class FoodCorner:
    def __init__(self):
        self.veg_combo_price = 120
        self.non_veg_combo_price = 150

    def calculate_bill_amount(self, food_type, quantity, distance):
        try:
            # Check if the inputs are valid
            if not (food_type == 'V' or food_type == 'N') or quantity < 1 or distance <= 0:
                raise ValueError("Invalid input. Please check the values provided.")
            
            # Calculate the cost per plate based on food type
            if food_type == 'V':
                cost_per_plate = self.veg_combo_price
            else:
                cost_per_plate = self.non_veg_combo_price

            # Calculate the delivery charge based on distance
            if distance <= 3:
                delivery_charge = 0
            elif distance <= 6:
                delivery_charge = 3 * (distance - 3)
            else:
                delivery_charge = 3 * 3 + 6 * (distance - 6)

            # Calculate the total bill amount
            total_amount = cost_per_plate * quantity + delivery_charge

            return total_amount
        except ValueError as e:
            print("Error:", str(e))
            return -1


# Create an instance of the FoodCorner class
restaurant = FoodCorner()

# Take input from the user for food type, quantity, and distance
try:
    food_type = input("Enter the type of food (V for vegetarian, N for non-vegetarian): ")
    quantity = int(input("Enter the quantity ordered: "))
    distance = float(input("Enter the distance in kilometers from the restaurant to the delivery point: "))

    # Call the calculate_bill_amount method to get the final bill amount
    bill_amount = restaurant.calculate_bill_amount(food_type, quantity, distance)

    # Check if the returned value is -1 (indicating invalid input) and display the appropriate message
    if bill_amount == -1:
        print("Invalid input. Please check the values provided.")
    else:
        print("Final bill amount to be paid: Rs", bill_amount)

except ValueError:
    print("Invalid input. Please enter valid values.")
