N, M = list(map(int, input().split()))

board = []

for i in range(N):
    line = list(input())
    for i in range(len(line)):
        if line[i] == "W":
            line[i] = 1
        else:
            line[i] = 0
    board.append(line)

while True:
    min_sum = 64
    for i in range(0, N - 7):
        for j in range(0, M - 7):
            sum = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if board[k][l] == 0:
                            sum += 1
                    else:
                        if board[k][l] == 1:
                            sum += 1
            if sum > 32:
                sum = 64 - sum
            if sum < min_sum:
                min_sum = sum
    break

print(min_sum)