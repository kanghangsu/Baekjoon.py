N = int(input())

DEVIL_NUMBER = 666

i = 1

titles = []
while True:
    if N == 1:
        print(DEVIL_NUMBER)
        break
    else:
        if "666" in str(i):
            titles.append(i)
            i += 1
        else:
            i += 1
        if len(titles) == N:
            print(titles[-1])
            break