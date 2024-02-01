# https://www.acmicpc.net/problem/10807

N, X = map(int, input().split())
nums = list(map(int, input().split()))

selectedNums = []

for i in range(N):
    if nums[i] < X:
        selectedNums.append(nums[i])

for i in range(len(selectedNums)):
    print(selectedNums[i], end=" ")

print()
