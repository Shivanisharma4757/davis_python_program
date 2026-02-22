# Number of rows
n = 5

for i in range(n, 0, -1):
    # Print leading spaces
    print(' ' * (n - i), end='')

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end='')

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()  # Move to next line

output
123454321
 1234321
  12321
   121
    1
