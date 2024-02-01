# https://www.acmicpc.net/problem/10798

matrix = []

for i in range(5):
    matrix.append(list(input()))

for i in range(15):
    for j in range(5):
        if len(matrix[j]) > i:
            print(matrix[j][i], end="")
print()
