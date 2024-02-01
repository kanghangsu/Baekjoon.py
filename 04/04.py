# https://www.acmicpc.net/problem/2562

nums = []

for i in range(9):
    nums.append(int(input()))

maxNum = max(nums)
maxIndex = nums.index(maxNum)

print(maxNum)
print(maxIndex + 1)
