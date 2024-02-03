# Import the necessary modules
from math import gcd

# Input A, B
A, B = map(int, input().split())

# Calculate the LCM of A and B
lcm = (A * B) // gcd(A, B)

# Print the LCM
print(str(lcm) + "\n")
