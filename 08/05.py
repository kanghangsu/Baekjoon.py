# https://www.acmicpc.net/problem/2292

N = int(input())

step = 1
max_num = 1

while True:
    max_num += (step - 1) * 6
    if N <= max_num:
        break
    step += 1

print(step)
