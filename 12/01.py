N, M = list(map(int, input().split()))
given_cards = sorted(list(map(int, input().split())))

sum_cards = []

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if given_cards[i] + given_cards[j] + given_cards[k] <= M:
                sum_cards.append(given_cards[i] + given_cards[j] + given_cards[k])

print(max(sum_cards))