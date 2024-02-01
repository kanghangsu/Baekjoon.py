# https://www.acmicpc.net/problem/10101

angles = []

for _ in range(3):
    angles.append(int(input()))

if sum(angles) == 180:
    if len(set(angles)) == 1:
        print("Equilateral")
    elif len(set(angles)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
