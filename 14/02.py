N, M = list(map(int, input().split()))

S = []

for i in range(N):
    S.append(input())

T = []
for i in range(M):
    T.append(input())

ans = 0
for i in range(N):
    if S[i] in T:
        ans += T.count(S[i])

print(ans)
