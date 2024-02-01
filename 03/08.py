T = int(input())
answers = []

for i in range(T):
    A, B = input().split()
    A = int(A)
    B = int(B)
    answer = f"Case #{i + 1}: {A} + {B} = {A + B}"
    answers.append(answer)

for answer in answers:
    print(answer)
