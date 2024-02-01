N, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(sorted(numbers)[-k])