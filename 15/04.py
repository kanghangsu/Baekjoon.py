# Import the necessary modules
from sys import stdin
from sys import stdout
from math import gcd

input = stdin.readline
print = stdout.write

# Input number of trees
N = int(input().rstrip())

trees = []
for i in range(N):
    trees.append(int(input().rstrip()))

# Sort the trees
trees.sort()

# Calculate the distance between the trees
distances = []
for i in range(1, N):
    distances.append(trees[i] - trees[i - 1])

# Calculate the GCD of the distances
gcd_distances = distances[0]
for i in range(1, len(distances)):
    gcd_distances = gcd(gcd_distances, distances[i])

# Count the number of trees to be planted
count = 0
for i in range(1, N):
    count += (trees[i] - trees[i - 1]) // gcd_distances - 1

# Print the number of trees to be planted
print(str(count) + "\n")
