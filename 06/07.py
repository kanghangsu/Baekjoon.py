# https://www.acmicpc.net/problem/1316

N = int(input())

count_group_words = 0

words = []
for i in range(N):
    words.append(input())

for i in range(N):
    word = words[i]

    for j in range(len(word)):
        try:
            if word[j] != word[j + 1]:
                if word[j + 1] in word[:j]:
                    break
        except:
            pass
    else:
        count_group_words += 1

print(count_group_words)
