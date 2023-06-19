'''
Q.20 Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total
price.(attributes item_id,item_name,quantity ) 
'''


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_id, item_name, quantity):
        item = {
            'item_id': item_id,
            'item_name': item_name,
            'quantity': quantity
        }
        self.items.append(item)
        print(f"Item '{item_name}' added to the shopping cart.")

    def remove_item(self, item_id):
        for item in self.items:
            if item['item_id'] == item_id:
                self.items.remove(item)
                print(
                    f"Item with ID '{item_id}' removed from the shopping cart.")
                return
        print(f"Item with ID '{item_id}' not found in the shopping cart.")

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            item_price = self.get_item_price(item['item_id'])
            total_price += item_price * item['quantity']
        return total_price

    def get_item_price(self, item_id):
        item_prices = {
            'item1': 10,
            'item2': 15,
            'item3': 20
        }
        return item_prices.get(item_id, 0)


cart = ShoppingCart()

cart.add_item('item1', 'Item 1', 2)
cart.add_item('item2', 'Item 2', 1)
cart.add_item('item3', 'Item 3', 3)

total_price = cart.calculate_total_price()
print("Total Price:", total_price)

cart.remove_item('item2')

total_price = cart.calculate_total_price()
print("Total Price:", total_price)