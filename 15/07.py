# Bertrand's postulate
# n: integer
# p: prime number
# There is at least one prime number between n and 2n

# Import the necessary modules
from sys import stdin
from sys import stdout

input = stdin.readline
print = stdout.write


# Eratosthenes' sieve
def sieve(max_number):
    # Create a list of booleans
    primes = [True] * (max_number + 1)

    # 0 and 1 are not prime numbers
    primes[0] = primes[1] = False

    # For each number from 2 to the square root of the maximum number
    for i in range(2, int(max_number**0.5) + 1):
        if primes[i]:

            # Mark all multiples of the number as not prime
            for j in range(i * i, max_number + 1, i):
                primes[j] = False
    return primes


# For each test case
while True:

    # Input n
    n = int(input().rstrip())

    # If n is 0, break
    if n == 0:
        break

    # Find the number of prime numbers between n and 2n
    primes = sieve(2 * n)

    # Count the number of prime numbers between n and 2n
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if primes[i]:
            count += 1

    # Print the number of prime numbers between n and 2n
    print(str(count) + "\n")
