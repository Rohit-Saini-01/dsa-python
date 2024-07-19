num = int(input("Enter the value of n:"))
row = 1
while row <= num:
    col = 1
    while col <= num - row:
        print(" ", end="")
        col += 1
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    row += 1
    print()
