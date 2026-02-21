# E-commerce Discount Engine Program

# Taking user inputs
cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

discount = 0  # Initial discount

# Cart value based discount
if cart_value >= 50000:
    discount = 20
elif cart_value >= 20000:
    discount = 10
elif cart_value >= 10000:
    discount = 5

# Membership based discount (highest discount will be applied)
if membership == "platinum":
    discount = max(discount, 25)
elif membership == "gold":
    discount = max(discount, 15)
elif membership == "silver":
    discount = max(discount, 10)

# Festival season discount
if festival == "yes":
    discount = max(discount, 30)

# Calculating final payable amount
final_amount = cart_value - (cart_value * discount / 100)

# Display results
print("Highest Discount Applied:", discount, "%")
print("Final Payable Amount: ₹", final_amount)
