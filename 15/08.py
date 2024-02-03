# Goldbach's partition

# Import the necessary modules
from sys import stdin, stdout

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


# Input number of test cases
T = int(input().rstrip())

# Initialize the maximum number
max_N = 10**6
prime_numbers = sieve(max_N)

# For each test case
for _ in range(T):

    # Input n
    N = int(input().rstrip())

    # Count the number of prime numbers between 2 and n
    count = 0
    for i in range(2, N // 2 + 1):
        if prime_numbers[i] and prime_numbers[N - i]:
            count += 1

    # Print the number of ways to partition n as the sum of two prime numbers
    print(str(count) + "\n")
