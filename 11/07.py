a_1, a_0 = list(map(int, input().split()))
c = int(input())
n_0 = int(input())


def f(n):
    return a_1 * n + a_0


def g(n):
    return n


condition = []

for n in range(n_0, 101):
    if f(n) <= c * g(n):
        condition.append(True)
    else:
        condition.append(False)

if False in condition:
    print(0)
else:
    print(1)