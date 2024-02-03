# Print prime numbers between M and N

# Import the necessary modules
from sys import stdin
from sys import stdout

input = stdin.readline
print = stdout.write

# Input M, N
N, M = map(int, input().rstrip().split())


# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Find the next prime number
for i in range(N, M + 1):
    if is_prime(i):
        print(str(i) + "\n")
