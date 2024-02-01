N = int(input())

longString = ""

for i in range(N // 4):
    longString = longString + "long "

print(longString + "int")
