# https://www.acmicpc.net/problem/5086

while True:
    try:
        a, b = map(int, input().split())
        if a % b == 0:
            print("multiple")
        elif b % a == 0:
            print("factor")
        else:
            print("neither")
    except:
        break
