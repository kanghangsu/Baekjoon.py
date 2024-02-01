T = int(input())
answers = []

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    answer = A + B
    answers.append(answer)

i = 0

for answer in answers:
    i = i + 1
    print(f"Case #{i}: {answer}")
