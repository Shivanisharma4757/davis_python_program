# Electricity Bill Calculator Program

# Taking input
units = float(input("Enter number of units consumed: "))
age = int(input("Enter your age: "))

bill = 0  # Initialize bill amount

# Calculating bill based on unit slabs
if units <= 100:
    bill = units * 5  # ₹5 per unit

elif units <= 300:
    bill = units * 7  # ₹7 per unit

else:
    bill = units * 10  # ₹10 per unit

# Applying 10% discount for senior citizens (age >= 60)
if age >= 60:
    discount = bill * 0.10
    bill = bill - discount
    print("Senior Citizen Discount Applied: ₹", discount)

# Display final bill
print("Total Electricity Bill: ₹", bill)
