# Number of rows
n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()  # Move to next line

#output
#12345
#1234
#123
#12
#1
