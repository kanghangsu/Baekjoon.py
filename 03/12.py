answers = []

while True:
    try:
        A, B = input().split()
        A = int(A)
        B = int(B)
        answer = A + B
        answers.append(answer)
    except:
        for answer in answers:
            print(answer)
        break
