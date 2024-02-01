def men_of_passion(A, n):
    sum = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                sum += A[i] * A[j] * A[k]  # CODE1
    return sum


# i : 1, 2, 3, ..., n-2
# j : i+1, i+2, ..., n-1
# k : j+1, j+2, ..., n

# i = 1, j = 2, k = 3 ~ n : n - 2
# i = 1, j = 3, k = 4 ~ n : n - 3
# ...
# i = 1, j = n - 1, k = n : 1
# => (n - 2) + (n - 3) + ... + 1 = (n - 1) * (n - 2) / 2

# i = 2, j = 3, k = 4 ~ n : n - 3
# i = 2, j = 4, k = 5 ~ n : n - 4
# ...
# i = 2, j = n - 1, k = n : 1
# => (n - 3) + (n - 4) + ... + 1 = (n - 2) * (n - 3) / 2

# (n-1)*(n-2)/2 + (n-2)*(n-3)/2 + ... + 1*0/2 = n*(n-1)*(n-2)/6

n = int(input())

print(int(n * (n - 1) * (n - 2) / 6))
print(3)