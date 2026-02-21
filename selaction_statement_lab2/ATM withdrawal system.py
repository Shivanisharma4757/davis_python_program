# ATM Withdrawal System Program

# Taking input
balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

# Check daily withdrawal limit (₹50,000)
if withdraw_amount > 50000:
    print("Withdrawal Failed: Exceeds daily withdrawal limit of ₹50,000.")

# Check sufficient balance
elif withdraw_amount > balance:
    print("Withdrawal Failed: Insufficient account balance.")

# Check ATM cash availability
elif withdraw_amount > atm_cash:
    print("Withdrawal Failed: Insufficient ATM cash available.")

# If all conditions satisfied
else:
    balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Withdrawal Successful!")
    print("Remaining Balance: ₹", balance)
