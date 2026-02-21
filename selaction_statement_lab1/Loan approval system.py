# Loan Approval System Program

# Taking input
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income: "))
existing_loans = float(input("Enter total existing loan amount: "))

# Checking credit score first

if credit_score < 600:
    print("Loan Rejected: Low Credit Score.")

elif credit_score >= 750:
    print("Loan Approved.")

else:
    # For credit score between 600 and 749
    # Additional income and loan check required
    
    if monthly_income < 30000 and existing_loans > 500000:
        print("Loan Rejected: Low Income and High Existing Loans.")
    else:
        print("Loan Approved after Income Verification.")
