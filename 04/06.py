# https://www.acmicpc.net/problem/10813

N, M = map(int, input().split())

baskets = []

for i in range(N):
    baskets.append(i + 1)

for c in range(M):
    i, j = map(int, input().split())
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(" ".join(map(str, baskets)))
