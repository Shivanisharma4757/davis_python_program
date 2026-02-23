# Number of rows
n = 5

for i in range(1, n + 1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    # Print stars
    print('*' * i)

#output
 #   *
  # **
  #***
 #****
#*****
