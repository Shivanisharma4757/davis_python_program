# Number of rows
n = 5

for i in range(n):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')
    
    # Calculate and print values in the row
    val = 1
    for j in range(i + 1):
        print(val, end=' ')
        val = val * (i - j) // (j + 1)  # Compute next value
    print()  # Move to next line

output
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
