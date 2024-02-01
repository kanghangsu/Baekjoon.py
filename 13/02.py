numbers = [int(input()) for _ in range(5)]

average = int(sum(numbers) / len(numbers))
middle = int(sorted(numbers)[len(numbers) // 2])

print(average)
print(middle)