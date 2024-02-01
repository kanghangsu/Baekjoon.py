import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
age_name = sorted(
    [input().rstrip().split() for _ in range(N)], key=lambda x: (int(x[0]))
)

print("\n".join([" ".join(age_name[i]) for i in range(N)]) + "\n")