# https://www.acmicpc.net/problem/2745

N, B = input().split()

AZ = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

revN = N[::-1]

result = 0

for i in range(len(revN)):
    result += AZ.index(revN[i]) * (int(B) ** i)

print(result)
