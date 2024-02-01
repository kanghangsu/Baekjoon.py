def men_of_passion(A, n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum += A[i] * A[j]  # CODE1
    return sum


n = int(input())

print(n**2)  #: (n * n)회 반복
print(2)