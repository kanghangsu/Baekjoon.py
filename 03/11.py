answers = []

while True:
    A, B = input().split()
    A = int(A)
    B = int(B)
    if A == 0 and B == 0:
        break
    else:
        answer = A + B
        answers.append(answer)

for answer in answers:
    print(answer)
