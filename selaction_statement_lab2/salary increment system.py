# Salary Increment System Program

# Taking input
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0  # Initialize increment percentage

# Performance based increment
if rating == 5:
    increment += 10
elif rating == 4:
    increment += 7
elif rating == 3:
    increment += 5
else:
    increment += 2

# Experience bonus
if experience >= 10:
    increment += 5
elif experience >= 5:
    increment += 3

# Attendance bonus
if attendance >= 95:
    increment += 3
elif attendance >= 85:
    increment += 2

# Display final increment
print("Total Increment Percentage:", increment, "%")
