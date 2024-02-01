# https://www.acmicpc.net/problem/1546

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

cheatScores = []
for i in range(N):
    cheatScores.append(scores[i] / M * 100)

cheatSum = 0
for i in range(N):
    cheatSum += cheatScores[i]

print(cheatSum / N)
