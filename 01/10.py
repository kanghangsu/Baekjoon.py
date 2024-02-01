A = int(input())
B = int(input())

ans3 = A * (B % 10)
ans4 = A * ((B % 100) // 10)
ans5 = A * (B // 100)
ans6 = A * B

print(ans3)
print(ans4)
print(ans5)
print(ans6)
