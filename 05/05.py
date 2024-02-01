# https://www.acmicpc.net/problem/11720

N = int(input())
S = input()

sum = 0

for _ in range(len(S)):
    sum += int(S[_])

print(sum)
