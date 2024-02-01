X = int(input())
N = int(input())

for i in range(N):
    perItem = input().split()
    a = int(perItem[0])
    b = int(perItem[1])
    X = X - a * b

if X == 0:
    print("Yes")
else:
    print("No")
