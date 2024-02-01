# https://www.acmicpc.net/problem/2675

T = int(input())

answers = []

for _ in range(T):
    R, S = input().split()
    R = int(R)
    answer = ""
    for c in S:
        answer += c * R
    answers.append(answer)

print("\n".join(answers))
