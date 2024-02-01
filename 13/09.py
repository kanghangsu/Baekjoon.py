N = int(input())

words = sorted(list(set([input() for _ in range(N)])), key=lambda x: (len(x), x))

print("\n".join(words))