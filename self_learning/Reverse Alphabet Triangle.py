# Number of rows
n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end='')  # 65 is ASCII of 'A'
    print()  # Move to next line

#output
#ABCDE
#ABCD
#ABC
#AB
#A
