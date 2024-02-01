# https://www.acmicpc.net/problem/2941

croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

LEN_WORD = len(word)

count_croatian_alphabet = 0

for i in range(len(croatian_alphabet)):
    if croatian_alphabet[i] in word:
        count_croatian_alphabet += word.count(croatian_alphabet[i])

print(LEN_WORD - count_croatian_alphabet)
