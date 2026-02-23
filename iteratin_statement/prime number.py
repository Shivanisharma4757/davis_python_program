# Program to check whether a number is prime or not

# Take input from the user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(num, "is not a prime number")

else:
    # Assume the number is prime
    is_prime = True

    # Check divisibility from 2 to square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If divisible, it is not prime
            is_prime = False
            break  # Exit loop immediately

    # Print result
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#output
#Enter a number: 13
#13 is a prime number
