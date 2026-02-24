# Program to print multiplication tables from 1 to 10

for i in range(1, 11):                     # Outer loop for numbers 1 to 10
    print("Table of", i)                   # Print table heading
    
    for j in range(1, 11):                 # Inner loop for multiplication
        print(i, "x", j, "=", i*j)         # Print multiplication result
    
    print()                                # Print blank line after each table

# Output Example
# Table of 1
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 1 x 10 = 10
#
# Table of 2
# 2 x 1 = 2
# ...
# 2 x 10 = 20
