# Find next prime number

# Import the necessary modules
from sys import stdin
from sys import stdout

input = stdin.readline
print = stdout.write

# Input number of test cases
T = int(input().rstrip())


# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to find the next prime number
def next_prime(n):
    while not is_prime(n):
        n += 1
    return n


# For each test case
for _ in range(T):
    # Input number
    N = int(input().rstrip())

    # Find the next prime number
    print(str(next_prime(N)) + "\n")
