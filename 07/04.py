# https://www.acmicpc.net/problem/2563

N = int(input())

filed = []

for i in range(100):
    filed.append([0] * 100)

for i in range(N):
    x, y = map(int, input().split())
    for j in range(y, y + 10):
        for k in range(x, x + 10):
            filed[j][k] = 1

result = 0

for i in range(100):
    for j in range(100):
        if filed[i][j] == 1:
            result += 1

print(result)
