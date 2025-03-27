# Define menu dictionary with items and prices
menu = {
    "apple" : 10,
    "mango" : 20,
    "banana": 30,
    "orange": 40,  
}

# Initialize date and get customer name
date = "March 12"
name = input("Enter the name: ").capitalize().strip()  # Capitalize and clean name input

# Initialize order tracking variables
recip = []      # List to store order details
total_ord = 0   # Variable to track total amount

# Print welcome message and menu
print(f"!!!!Welocome to Ram BABA Dhava!!!!\n{"":<4}====MENU=====")
for item, price in menu.items():
    print(f"--> {item.capitalize():<10} --{price}")  # Format menu display
print(f"\n{"":<2} Order the food \n")

# Main order taking loop
while True:
    # Get customer order input (lowercase and stripped of whitespace)
    customer = input("What Do you want sir(if not enter 'done'): ").lower().strip()
    
    # Exit condition
    if customer == "done":
        break
    
    # Input validation - check if item exists in menu
    if not customer.isalpha() or customer not in menu:
        print("We do not have that, please order the things which are in the menu\n")
        for item in menu:
            print(f"--> {item.capitalize():<10}--")  # Show available items
        continue
    
    # Quantity input loop
    while True:
        quantity = input(f"How many {customer} : ")
        if quantity.isdigit():  # Check if input is numeric
            quantity_int = int(quantity)
            # Calculate and update order total
            total_ord += menu[customer]*quantity_int
            # Add order details to receipt list (item, quantity, running total)
            recip.append((customer, quantity, total_ord))
            break
        else:
            continue  # Repeat if quantity is not numeric

# Receipt generation
if recip:  # Check if any orders were placed
    print('-'*25)
    print(f"{date}")
    print(f"Name: {name}")
    print("-"*25)
    print("order:")
    # Print each ordered item
    for item, qty, toto in recip:
        print(f"{item.capitalize():<10} --x{qty}")
    print("="*25)
    print(f"Total {toto}")
    
    # Save order to file
    with open("Sell record.txt", 'a') as f:
        f.write(f"{date}\nName:{name}\n")
        f.write("-"*25 + "\n")
        f.write("order:\n")
        for item, qty, toto in recip:
            f.write(f"{item.capitalize():<10} --x{qty}\n")
        f.write(f"Total bill amount: {toto}\n")
        f.write("="*25 + "\n\n")
else:
    print("NO order")  # Message if no orders were placed