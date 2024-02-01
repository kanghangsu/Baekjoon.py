import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
numbers = [int(input().rstrip()) for _ in range(N)]
sorted_numbers = sorted(numbers)

for i in range(N):
    print(str(sorted_numbers[i]) + "\n")