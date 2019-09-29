# The number we will perform the collatz operation
n = int(input("Enter a positive integer: "))

# Keep looping until we reach 1.
# Note: this assuemes the Collatz conjecture is true
while n != 1:
    # Print the current value of n 
    print(n)
    # Check if n is even
    if n % 2 == 0:
        # If n is even, divide it by two.
        n = n // 2
    else:
        # If n is odd, multiplay by three and add 1.
        n = (3 * n) + 1

#Finally, print the 1.
print(n)