# https://www.acmicpc.net/problem/3052

nums = []
mods = []

for i in range(10):
    nums.append(int(input()))

for i in range(10):
    if nums[i] % 42 not in mods:
        mods.append(nums[i] % 42)

print(len(mods))
