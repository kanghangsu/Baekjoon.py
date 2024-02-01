# https://www.acmicpc.net/problem/11718

buffer = []

while True:
    try:
        buffer.append(input())
    except:
        break

print("\n".join(buffer))
