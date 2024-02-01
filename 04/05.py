# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())

baskets = []

for i in range(N):
    baskets.append(0)

for c in range(M):
    i, j, k = map(int, input().split())
    for d in range(i - 1, j):
        baskets[d] = k

print(" ".join(map(str, baskets)))
