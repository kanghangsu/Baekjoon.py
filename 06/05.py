# https://www.acmicpc.net/problem/1157

word = input().upper()

LEN_WORD = len(word)

letters = []

for i in range(LEN_WORD):
    letter = word[i]
    if letter not in letters:
        letters.append(letter)

count_letters = []

for i in range(len(letters)):
    count_letters.append(word.count(letters[i]))

max_count = max(count_letters)

if count_letters.count(max_count) > 1:
    print("?")
else:
    print(letters[count_letters.index(max_count)])
