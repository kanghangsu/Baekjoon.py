# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

prime_numbers = []

for number in range(M, N + 1):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        prime_numbers.append(number)

if len(prime_numbers) == 0:
    print(-1)

else:
    print(sum(prime_numbers))
    print(min(prime_numbers))
