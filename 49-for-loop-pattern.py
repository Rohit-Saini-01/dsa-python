n = int(input("ENter the value of the num:"))

for i in range(n):
    if i % 2 == 0:
        for j in range(n - i):
            print(1, end="")
    else:
        for j in range(n - i):
            print(0, end="")
    print()
