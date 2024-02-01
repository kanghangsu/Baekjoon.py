def men_of_passion(A, n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                sum += A[i] * A[j] * A[k]  # CODE1
    return sum

# i: 1, 2, 3, ..., n
# j: 1, 2, 3, ..., n
# k: 1, 2, 3, ..., n
# n * n * n = n**3

n = int(input())

print(n**3)
print(3)