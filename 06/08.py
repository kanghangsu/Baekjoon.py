# https://www.acmicpc.net/problem/25206

subjects = []
credits = []
grades = []

for i in range(20):
    S = input()
    subject = S.split()[0]
    credit = float(S.split()[1])
    grade = S.split()[2]
    subjects.append(subject)
    credits.append(credit)
    grades.append(grade)

A_PLUS = 4.5
A_ZERO = 4.0
B_PLUS = 3.5
B_ZERO = 3.0
C_PLUS = 2.5
C_ZERO = 2.0
D_PLUS = 1.5
D_ZERO = 1.0
F = 0.0


def get_grade_point(grade):
    if grade == "A+":
        return A_PLUS
    elif grade == "A0":
        return A_ZERO
    elif grade == "B+":
        return B_PLUS
    elif grade == "B0":
        return B_ZERO
    elif grade == "C+":
        return C_PLUS
    elif grade == "C0":
        return C_ZERO
    elif grade == "D+":
        return D_PLUS
    elif grade == "D0":
        return D_ZERO
    elif grade == "F":
        return F
    elif grade == "P":
        return 0


sum_grade_point = 0

for i in range(20):
    if grades[i] == "P":
        credits[i] = 0
    sum_grade_point += float(credits[i]) * get_grade_point(grades[i])

print(sum_grade_point / sum(credits))
