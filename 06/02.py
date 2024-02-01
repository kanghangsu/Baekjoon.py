# https://www.acmicpc.net/problem/3003

PICESES = [1, 1, 2, 2, 2, 8]
piceses_has = list(map(int, input().split()))

for i in range(len(PICESES)):
    print(PICESES[i] - piceses_has[i], end=" ")

print()
