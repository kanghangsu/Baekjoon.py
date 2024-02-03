# Import the necessary modules
from sys import stdin
from sys import stdout
from math import gcd

input = stdin.readline
print = stdout.write

# Input fractions A, B
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

numerator_A = A[0]
denominator_A = A[1]

numerator_B = B[0]
denominator_B = B[1]

# Calculate A + B
numerator_sum = (numerator_A * denominator_B) + (numerator_B * denominator_A)
denominator_sum = denominator_A * denominator_B

# Calculate the GCD of the numerator and denominator
gcd_sum = gcd(numerator_sum, denominator_sum)

# reduce the fraction
numerator_sum //= gcd_sum
denominator_sum //= gcd_sum

# Print the sum
print(str(numerator_sum) + " " + str(denominator_sum) + "\n")
