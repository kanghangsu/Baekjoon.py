# https://www.acmicpc.net/problem/9063

N = int(input())

x, y = [], []

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)

size = (x_max - x_min) * (y_max - y_min)

print(size)
