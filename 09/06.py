# https://www.acmicpc.net/problem/11653

N = int(input())

divisors = []

i = 2

while N > 1:
    if N % i == 0:
        divisors.append(i)
        N //= i

    else:
        i += 1

for divisor in divisors:
    print(divisor)
