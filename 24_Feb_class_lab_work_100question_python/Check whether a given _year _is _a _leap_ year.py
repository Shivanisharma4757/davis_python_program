# Problem 11
# Program to check whether a given year is a leap year

# Taking input from the user
year = int(input("Enter a year: "))

# Checking leap year condition
# A year is a leap year if:
# 1. It is divisible by 4 AND
# 2. Not divisible by 100 UNLESS it is also divisible by 400

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

#output
#Enter a year: 2022
#2022 is not a Leap Year
