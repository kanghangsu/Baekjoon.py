import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

sorted_set_A = sorted(list(set(A)))
D = {sorted_set_A[i]: i for i in range(len(sorted_set_A))}

print(" ".join(map(str, [D[i] for i in A])))