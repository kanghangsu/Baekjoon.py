# Import the necessary modules
from sys import stdin
from sys import stdout

input = stdin.readline
print = stdout.write

# Input S: the string
S = input().rstrip()

# Count the number of substrings of S that are unique
substrings = []

for i in range(len(S)):
    for j in range(i, len(S)):
        substrings.append(S[i : j + 1])

unique_substrings = set(substrings)

# Print the number of unique substrings
print(str(len(unique_substrings)) + "\n")
