# https://www.acmicpc.net/problem/9086

T = int(input())
answers = []

for _ in range(T):
    S = input()
    answers.append(S[0] + S[-1])

print("\n".join(answers))
