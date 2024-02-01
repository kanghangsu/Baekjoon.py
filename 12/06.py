N = int(input())

sugars = []

small_sugar = 3
big_sugar = 5

for i in range(0, N // small_sugar + 1):
    for j in range(0, N // big_sugar + 1):
        if small_sugar * i + big_sugar * j == N:
            sugars.append(i + j)

if len(sugars) == 0:
    print(-1)
else:
    print(min(sugars))