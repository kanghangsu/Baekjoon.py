# https://www.acmicpc.net/problem/10818

N = int(input())
nums = list(map(int, input().split()))

minNum = min(nums)
maxNum = max(nums)

print(minNum, maxNum)
