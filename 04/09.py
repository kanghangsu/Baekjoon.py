# https://www.acmicpc.net/problem/10811

N, M = map(int, input().split())

baskets = []

for i in range(N):
    baskets.append(i + 1)

for c in range(M):
    i, j = map(int, input().split())
    baskets[i - 1 : j] = baskets[i - 1 : j][::-1]

print(" ".join(map(str, baskets)))
