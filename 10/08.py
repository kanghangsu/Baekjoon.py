# https://www.acmicpc.net/problem/14215

lengths = list(map(int, input().split()))

a = sorted(lengths)[0]
b = sorted(lengths)[1]
c = sorted(lengths)[2]

if a + b > c:
    print(a + b + c)
else:
    print((a + b) - 1 + a + b)
