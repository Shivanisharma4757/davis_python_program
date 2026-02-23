# Income Tax Calculator Program

# Taking user input
income = float(input("Enter annual income: "))
age = int(input("Enter age: "))

# Setting exemption limit based on age
# Senior citizens (age >= 60) get ₹3,00,000 exemption
# Others get ₹2,50,000 exemption

if age >= 60:
    exemption = 300000
else:
    exemption = 250000

tax = 0  # Initial tax value

# Calculating tax based on slabs

if income <= exemption:
    tax = 0  # No tax within exemption limit

elif income <= 500000:
    tax = (income - exemption) * 0.05  # 5% tax

elif income <= 1000000:
    tax = (500000 - exemption) * 0.05 + (income - 500000) * 0.20

else:
    tax = (500000 - exemption) * 0.05 + \
          (1000000 - 500000) * 0.20 + \
          (income - 1000000) * 0.30

# Displaying final tax
print("Total Tax to Pay: ₹", tax)
#output
#Enter annual income: 200000
#Enter age: 30
#Total Tax to Pay: ₹ 0
