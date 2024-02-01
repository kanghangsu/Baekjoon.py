# https://www.acmicpc.net/problem/10809

S = input()

AZ = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(AZ)):
    if AZ[i] in S:
        print(S.index(AZ[i]), end=" ")
    else:
        print(-1, end=" ")
print()
