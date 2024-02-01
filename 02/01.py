numbers = input().split()

A = int(numbers[0])
B = int(numbers[1])

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
