import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
s = set()

for i in range(n):
    name, action = input().split()
    if action == "enter":
        s.add(name)
    else:
        s.remove(name)

print("\n".join(sorted(s, reverse=True)) + "\n")
