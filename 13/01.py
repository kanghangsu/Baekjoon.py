N = int(input())

numbers = [int(input()) for _ in range(N)]

for i in range(N):
    print(sorted(numbers)[i])