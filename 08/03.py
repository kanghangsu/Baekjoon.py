# https://www.acmicpc.net/problem/2720

T = int(input())

C = []

for i in range(T):
    C.append(int(input()))

for i in range(T):
    Q = C[i] // 25
    C[i] -= Q * 25
    D = C[i] // 10
    C[i] -= D * 10
    N = C[i] // 5
    C[i] -= N * 5
    P = C[i] // 1
    C[i] -= P * 1
    print(Q, D, N, P)
