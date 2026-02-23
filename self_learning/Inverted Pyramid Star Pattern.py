# Number of rows
n = 5

for i in range(n, 0, -1):
    # Print leading spaces
    print(' ' * (n - i), end='')
    # Print stars
    print('*' * (2 * i - 1))

#output
#*********
 #*******
  #*****
   #***
    #*
