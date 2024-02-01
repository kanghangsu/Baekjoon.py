def men_of_passion(A, n):
    count = 0
    sum = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            count += 1
            sum += A[i] * A[j]
    return sum, count


n = int(input())

# i: 1, 2, 3, ..., n-1
# j: i+1, i+2, ..., n
# i가 1일 때, j는 2 ~ n : n - 1
# i가 2일 때, j는 3 ~ n : n - 2
# i가 3일 때, j는 4 ~ n : n - 3
# ...
# i가 n-1일 때, j는 n : 1
# (n - 1) + (n - 2) + ... + 1 = n * (n - 1) / 2

print(int(n * (n - 1) / 2))
print(2)