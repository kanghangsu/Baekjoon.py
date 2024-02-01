N = int(input())

constructor = []

for i in range(1, N + 1):
    if i + sum(map(int, str(i))) == N:
        constructor.append(i)

if len(constructor) == 0:
    print(0)

else:
    print(min(constructor))