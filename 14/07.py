# Import
from sys import stdin
from sys import stdout

input = stdin.readline
print = stdout.write

# Input elem_of_A, elem_of_B, A, B
elem_of_A, elem_of_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# (A - B) or (B - A)
sym_dif_A_B = (A - B) | (B - A)

# Print the length of sym_dif_A_B
print(str(len(sym_dif_A_B)) + "\n")
