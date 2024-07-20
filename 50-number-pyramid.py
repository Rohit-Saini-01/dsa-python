n = int(input())

for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end="")
    for j in range(i, n + 1):
        print(j, end="")
    print()
for i in range(1, n):
    for j in range(n - i + 1, 2, -1):
        print(" ", end="")
    for j in range(n - i, n + 1):
        print(j, end="")
    print()
