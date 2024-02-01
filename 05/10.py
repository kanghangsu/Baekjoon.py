# https://www.acmicpc.net/problem/5622

S = input()

AZ = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0

for i in range(len(S)):
    for j in range(len(AZ)):
        if S[i] in AZ[j]:
            time += j + 3

print(time)
