# https://www.acmicpc.net/problem/11005

N, B = map(int, input().split())

AZ = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""

while N > 0:
    result = result + AZ[N % B]
    N = N // B

print(result[::-1])
