import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
# C = list(map(int, input().split()))
C = set(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

ans = []

for i in range(M):
    if A[i] in C:
        ans.append(1)
    else:
        ans.append(0)

print(" ".join(map(str, ans)) + "\n")

# list: list = [1, 2, 3, 4, 5]
# tuple: tuple = (1, 2, 3, 4, 5)
# dict: dict = {"key1": val1, "key2": val2, "key3": val3, "key4": val4, "key5": val5}
# set: set = {"key1", "key2", "key3", "key4", "key5"}
