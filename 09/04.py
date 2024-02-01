# https://www.acmicpc.net/problem/1978

N = int(input())

numbers = list(map(int, input().split()))

prime_numbers = []

for number in numbers:
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        prime_numbers.append(number)

print(len(prime_numbers))
