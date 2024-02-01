import sys

T = int(sys.stdin.readline().rstrip())
answers = []

for i in range(T):
    A, B = sys.stdin.readline().rstrip().split()
    A = int(A)
    B = int(B)
    answer = A + B
    answers.append(answer)

for answer in answers:
    print(answer)
