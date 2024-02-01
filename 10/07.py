# https://www.acmicpc.net/problem/5073

while True:
    try:
        lengths = list(map(int, input().split()))
        if set(lengths) == {0}:
            break
        else:
            if sum(lengths) - max(lengths) <= max(lengths):
                print("Invalid")
            elif len(set(lengths)) == 1:
                print("Equilateral")
            elif len(set(lengths)) == 2:
                print("Isosceles")
            else:
                print("Scalene")
    except:
        break
