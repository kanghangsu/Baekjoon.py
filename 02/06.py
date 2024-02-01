nowHM = input().split()
cookM = int(input())

nowH = int(nowHM[0])
nowM = int(nowHM[1])

nowMM = nowH * 60 + nowM

alramMM = nowMM + cookM

if alramMM >= 24 * 60:
    alramMM = alramMM - 24 * 60

alramH = alramMM // 60
alramM = alramMM % 60

print(alramH, alramM)
