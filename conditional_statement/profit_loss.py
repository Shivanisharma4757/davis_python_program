# Program to calculate Profit or Loss and its Percentage
# With comments and basic input validation

# Taking input from user
cost_price_input = input("Enter Cost Price: ")
selling_price_input = input("Enter Selling Price: ")

# Validation: Check if inputs are numeric
if cost_price_input.replace('.', '', 1).isdigit() and selling_price_input.replace('.', '', 1).isdigit():
    
    cost_price = float(cost_price_input)
    selling_price = float(selling_price_input)

    # Validation: Cost price must be greater than 0
    if cost_price > 0:
        
        # If Selling Price is greater than Cost Price → Profit
        if selling_price > cost_price:
            profit = selling_price - cost_price
            profit_percent = (profit / cost_price) * 100
            
            print("\nProfit: ₹", profit)
            print("Profit Percentage:", round(profit_percent, 2), "%")
        
        # If Selling Price is less than Cost Price → Loss
        elif selling_price < cost_price:
            loss = cost_price - selling_price
            loss_percent = (loss / cost_price) * 100
            
            print("\nLoss: ₹", loss)
            print("Loss Percentage:", round(loss_percent, 2), "%")
        
        # If both are equal → No Profit No Loss
        else:
            print("\nNo Profit No Loss.")
    
    else:
        print("Error: Cost Price must be greater than 0.")

else:
    print("Error: Please enter valid numeric values.")
#output
#Enter Cost Price: 1000
#Enter Selling Price: 1200

#Profit: ₹ 200.0
#Profit Percentage: 20.0 %
