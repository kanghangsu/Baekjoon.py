targetHM = input().split()

targetH = int(targetHM[0])
targetM = int(targetHM[1])

targetMM = targetH * 60 + targetM

alramMM = targetMM - 45

if alramMM < 0:
    alramMM = alramMM + 24 * 60

alramH = alramMM // 60
alramM = alramMM % 60

print(alramH, alramM)
