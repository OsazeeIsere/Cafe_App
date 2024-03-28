"""
The following python program manages the stock in a cafe
The list data structure holds each items in the menu
the dictionary data structure is used to hold the key:value pairs of both the 
stock of each item and another dictionary to hold the corresponding prices of the items in stock 
Eventually, the total worth of the stock is calculated and printed
"""
# The main program brgins
def ShowMenu(menuitems):
    
    # Print keys and values formatted
    for items, price in menuitems.items():
        print(f"Menu: {items}, Price: £{price}")    


def SelectMenu(menu, item, quantity):
    """
Calculate the total cost of the selected item(s).
    """
    if item in menu:
        price = menu[item]
        total_cost = price * quantity
        return total_cost
    else:
        return None
    
menu = ['Coffee', 'Checken', 'Sandwiches', 'Soups and salads', 'Pastries and desserts'] # the cafe menu list

stock = {'Coffee':12, # The dictionary holding the available stock of each item in the menu as key:value pairs
         'Checken': 15,
         'Sandwiches': 100,
         'Soups and salads': 30,
         'Pastries and desserts': 50
              
        }

price = {'Coffee':3, # The dictionary holding the prices of each item in the menu as key:value pairs
         'Checken': 2.50,
         'Sandwiches': 4.30,
         'Soups and salads': 7,
         'Pastries and desserts': 5     
        }
# Here we call the method to display the menu
ShowMenu(price)

# Get user input
selected_item = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity you want to buy: "))

 # Calculate cost
total_cost = SelectMenu(price, selected_item, quantity)
if total_cost is not None:
    print(f"Total cost for {quantity} {selected_item}(s): ${total_cost}")
else:
    print("Invalid item selected.")

""" total_stock = 0.0

# looping through the menu list to get each item
for item in menu:
    item_value = (stock[item] * price[item]) # Each ‘item_value’ is calculated by multiplying the stock value by the price value.
    total_stock += item_value

 
total_stock = round(total_stock,2) # the next statement Rounds up total stock value to two decimal places
print(f"The total stock in the cafe is worth: £{total_stock}p")  """