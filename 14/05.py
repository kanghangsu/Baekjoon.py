N = int(input())
N_nums = list(map(int, input().split()))

M = int(input())
M_nums = list(map(int, input().split()))

count_N_nums = {}
for num in N_nums:
    if num in count_N_nums:
        count_N_nums[num] += 1
    else:
        count_N_nums[num] = 1

for num in M_nums:
    if num in count_N_nums:
        print(count_N_nums[num], end=" ")
    else:
        print(0, end=" ")
print()
