# https://www.acmicpc.net/problem/10988

word = input()
LEN_WORD = len(word)

IS_PALINDROME = 1
NOT_PALINDROME = 0

IS_MATCH = []

if LEN_WORD % 2 == 0:
    for i in range(int(LEN_WORD / 2)):
        if word[i] == word[LEN_WORD - 1 - i]:
            IS_MATCH.append(IS_PALINDROME)
        else:
            IS_MATCH.append(NOT_PALINDROME)
else:
    for i in range(int((LEN_WORD - 1) / 2)):
        if word[i] == word[LEN_WORD - 1 - i]:
            IS_MATCH.append(IS_PALINDROME)
        else:
            IS_MATCH.append(NOT_PALINDROME)

if NOT_PALINDROME in IS_MATCH:
    print(NOT_PALINDROME)
else:
    print(IS_PALINDROME)
