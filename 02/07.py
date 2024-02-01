dices = input().split()

dice1 = int(dices[0])
dice2 = int(dices[1])
dice3 = int(dices[2])

if dice1 == dice2 and dice2 == dice3:
    price = 10000 + dice1 * 1000
elif dice1 == dice2:
    price = 1000 + dice1 * 100
elif dice2 == dice3:
    price = 1000 + dice2 * 100
elif dice1 == dice3:
    price = 1000 + dice1 * 100
else:
    price = max(dice1, dice2, dice3) * 100

print(price)
