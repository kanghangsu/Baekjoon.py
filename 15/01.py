# Import the necessary modules
from sys import stdin
from sys import stdout
from math import gcd

input = stdin.readline
print = stdout.write

# Input T: the number of test cases
T = int(input())

# For each test case
for _ in range(T):
    # Input N, M
    N, M = map(int, input().split())

    # Calculate the LCM of N and M
    lcm = (N * M) // gcd(N, M)

    # Print the LCM
    print(str(lcm) + "\n")
