"""
The following python program manages the stock in a cafe
The list data structure holds each items in the menu
the dictionary data structure is used to hold the key:value pairs of both the 
stock of each item and another dictionary to hold the corresponding prices of the items in stock 
Eventually, the total worth of the stock is calculated and printed
"""
# The main program brgins

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

total_stock = 0.0

# looping through the menu list to get each item
for item in menu:
    item_value = (stock[item] * price[item]) # Each ‘item_value’ is calculated by multiplying the stock value by the price value.
    total_stock += item_value

 
total_stock = round(total_stock,2) # the next statement Rounds up total stock value to two decimal places
print(f"The total stock in the cafe is worth: £{total_stock}p") 