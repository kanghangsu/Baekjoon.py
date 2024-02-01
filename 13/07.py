N = int(input())

cordination = [list(map(int, input().split())) for _ in range(N)]
cordination.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(cordination[i][0], cordination[i][1])