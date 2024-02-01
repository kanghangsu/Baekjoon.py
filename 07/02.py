# https://www.acmicpc.net/problem/2566

matrix = []

for i in range(9):
    matrix.append(list(map(int, input().split())))

M = 0
M_i = 0  # 변수를 미리 선언해두지 않으면, M_i, M_j가 선언되지 않았다는 오류가 발생한다.
M_j = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > M:
            M = matrix[i][j]
            M_i = i
            M_j = j

print(M)
print(M_i + 1, M_j + 1)
