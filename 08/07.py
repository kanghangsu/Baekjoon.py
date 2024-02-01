# https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())

N = (V - A) // (A - B)
if (V - A) % (A - B) != 0:
    N += 1
if A + N * (A - B) >= V:
    print(N + 1)
