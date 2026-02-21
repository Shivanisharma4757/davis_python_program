# Program to Calculate Total Shopping Bill
# Calculates total amount based on item price and quantity

total_bill = 0  # Variable to store final total amount

# Taking number of items
num_items_input = input("Enter number of items: ")

# Validation: Check if number of items is a valid integer
if num_items_input.isdigit():
    
    num_items = int(num_items_input)
    
    if num_items > 0:
        
        # Loop for each item
        for i in range(1, num_items + 1):
            
            print("\nItem", i)
            
            price_input = input("Enter price of item: ")
            quantity_input = input("Enter quantity: ")
            
            # Validate price and quantity
            if price_input.replace('.', '', 1).isdigit() and quantity_input.isdigit():
                
                price = float(price_input)
                quantity = int(quantity_input)
                
                if price >= 0 and quantity > 0:
                    
                    item_total = price * quantity  # Calculate item total
                    total_bill += item_total       # Add to final bill
                    
                    print("Item Total: ₹", item_total)
                
                else:
                    print("Invalid price or quantity. Skipping this item.")
            
            else:
                print("Invalid input. Skipping this item.")
        
        # Display final total bill
        print("\n----- Final Bill -----")
        print("Total Amount to Pay: ₹", total_bill)
    
    else:
        print("Number of items must be greater than 0.")

else:
    print("Error: Please enter a valid number of items.")
