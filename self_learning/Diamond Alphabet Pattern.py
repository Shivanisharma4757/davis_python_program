# Number of rows for top half
n = 5

# Top half of diamond
for i in range(1, n + 1):
    # Leading spaces
    print(' ' * (n - i), end='')

    # Increasing letters
    for j in range(i):
        print(chr(65 + j), end='')

    # Decreasing letters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end='')

    print()  # Move to next line

# Bottom half of diamond
for i in range(n - 1, 0, -1):
    # Leading spaces
    print(' ' * (n - i), end='')

    # Increasing letters
    for j in range(i):
        print(chr(65 + j), end='')

    # Decreasing letters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end='')

    print()  # Move to next line

output

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
 ABCDCBA
  ABCBA
   ABA
    A
