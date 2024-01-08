print('''
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝''')

import random

class VendingMachine:
    def __init__(self):
        # Define the menu with items, codes, and prices
        self.menu = {
            'A1': {'name': 'Red Bull Energy Drink', 'category': 'Drinks', 'price': 13.00, 'stock': 10},
            'A2': {'name': 'Red Bull Sugarfree', 'category': 'Drinks', 'price': 10.00, 'stock': 10},
            'A3': {'name': 'Red Bull Red Edition', 'category': 'Drinks', 'price': 10.00, 'stock': 10},
            'A4': {'name': 'Red Bull Blue Edition', 'category': 'Drinks', 'price': 10.50, 'stock': 10},
            'A5': {'name': 'Red Bull Yellow Edition', 'category': 'Drinks', 'price': 10.50, 'stock': 10},
            'A6': {'name': 'Aquafina Water', 'category': 'Drinks', 'price': 1.00, 'stock': 15},
            'A7': {'name': 'Pocari Sweat', 'category': 'Drinks', 'price': 6.25, 'stock': 12},
            'A8': {'name': 'Gatorade Lemonade', 'category': 'Drinks', 'price': 5.25, 'stock': 8},
            'A9': {'name': 'Gatorade Cool Blue', 'category': 'Drinks', 'price': 5.25, 'stock': 8},
            'A10': {'name': 'Gatorade Orange', 'category': 'Drinks', 'price': 5.25, 'stock': 8},
            'A11': {'name': 'Gatorade Glacier Cherry Zero Sugar', 'category': 'Drinks', 'price': 5.50, 'stock': 8},
            'A12': {'name': 'Gatorade Strawberry', 'category': 'Drinks', 'price': 5.25, 'stock': 8},
            'B1': {'name': 'Lays Classic', 'category': 'Chips', 'price': 6.00, 'stock': 12},
            'B2': {'name': 'Lays Salt and Vinegar', 'category': 'Chips', 'price': 7.50, 'stock': 12},
            'B3': {'name': 'Lays Barbecue', 'category': 'Chips', 'price': 7.50, 'stock': 12},
            'B4': {'name': 'Lays Sour Cream and Onion', 'category': 'Chips', 'price': 5.00, 'stock': 12},
            'B5': {'name': 'Lays Chili', 'category': 'Chips', 'price': 6.00, 'stock': 12},
            'B6': {'name': 'Pringles Original', 'category': 'Chips', 'price': 4.75, 'stock': 10},
            'B7': {'name': 'Pringles Sour Cream and Onion', 'category': 'Chips', 'price': 3.25, 'stock': 10},
            'B8': {'name': 'Pringles Cheddar Cheese', 'category': 'Chips', 'price': 8.00, 'stock': 10},
            'B9': {'name': 'Pringles Pizza', 'category': 'Chips', 'price': 3.00, 'stock': 10},
            'B10': {'name': 'Pringles Salt and Vinegar', 'category': 'Chips', 'price': 4.75, 'stock': 10},
            'B11': {'name': 'Doritos Nacho Cheese', 'category': 'Chips', 'price': 8.00, 'stock': 9},
            'B12': {'name': 'Doritos Cool Ranch', 'category': 'Chips', 'price': 10.50, 'stock': 9},
            'B13': {'name': 'Doritos Spicy Sweet Chili', 'category': 'Chips', 'price': 7.25, 'stock': 9},
            'B14': {'name': 'Doritos FLAMAS', 'category': 'Chips', 'price': 9.00, 'stock': 9},
            'B15': {'name': 'Doritos Salsa Verde', 'category': 'Chips', 'price': 14.00, 'stock': 9},
            'C1': {'name': 'KitKat', 'category': 'Chocolate Bars', 'price': 1.50, 'stock': 15},
            'C2': {'name': 'Galaxy', 'category': 'Chocolate Bars', 'price': 3.50, 'stock': 14},
            'C3': {'name': 'Hersheys', 'category': 'Chocolate Bars', 'price': 3.50, 'stock': 12},
            'C4': {'name': 'Snickers', 'category': 'Chocolate Bars', 'price': 2.00, 'stock': 15},
            'C5': {'name': 'Twix', 'category': 'Chocolate Bars', 'price': 3.25, 'stock': 12},
            'D1': {'name': 'M&Ms', 'category': 'Candy', 'price': 4.00, 'stock': 15},
            'D2': {'name': 'Haribo Goldbears', 'category': 'Candy', 'price': 5.00, 'stock': 10},
            'D3': {'name': 'Skittles', 'category': 'Candy', 'price': 2.75, 'stock': 15},
            'D4': {'name': 'Reeses Peanut Butter Cups', 'category': 'Candy', 'price': 3.75, 'stock': 8},
            'D5': {'name': 'Sour Patch Kids', 'category': 'Candy', 'price': 3.00, 'stock': 10},
        }
        self.money_inserted = 0.0

    def display_menu(self):
        print("===== Vending Machine Menu =====")
        for code, item in self.menu.items():
            print(f"{code}: {item['name']} ({item['category']}) - AED {item['price']} - Stock: {item['stock']}")

    def insert_money(self):
        try:
            self.money_inserted = float(input("Insert money (in dirhams): "))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def select_item(self):
        code = input("Enter the code of the item you want to purchase: ")
        item = self.menu.get(code)

        if item and item['stock'] > 0:
            if self.money_inserted >= item['price']:
                self.money_inserted -= item['price']
                item['stock'] -= 1
                print(f"Dispensing {item['name']}...")

                # Check for suggestions
                self.suggest_purchase(item['category'])

                print(f"Remaining balance: AED {self.money_inserted:.2f}")
            else:
                print("Insufficient funds. Please insert more money.")
        elif item and item['stock'] == 0:
            print(f"Sorry, {item['name']} is out of stock.")
        else:
            print("Invalid code. Please enter a valid code.")

    def suggest_purchase(self, category):
        # Basic suggestion system
        suggestions = [item['name'] for code, item in self.menu.items() if item['category'] == category and item['stock'] > 0]
        if suggestions:
            suggestion = random.choice(suggestions)
            print(f"Consider adding {suggestion} to your purchase!")

    def return_change(self):
        if self.money_inserted > 0:
            print(f"Returning change: AED {self.money_inserted:.2f}")
            self.money_inserted = 0.0

    def run(self):
        while True:
            self.display_menu()
            self.insert_money()
            self.select_item()
            self.return_change()

            cont = input("Do you want to buy more items? (yes/no): ").lower()
            if cont != 'yes':
                print("Thank you for using the Vending Machine. Have a great day!")
                break

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
      
   