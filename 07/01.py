# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())

matrixA = []
matrixB = []

for i in range(N):
    matrixA.append(list(map(int, input().split())))
for i in range(N):
    matrixB.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        matrixA[i][j] += matrixB[i][j]

for i in range(N):
    for j in range(M):
        print(matrixA[i][j], end=" ")
    print()
