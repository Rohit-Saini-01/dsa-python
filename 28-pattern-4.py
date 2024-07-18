num = int(input("Enter the value of n:"))

row = 1
while row <= num:
    col = 1
    while col <= row:
        print(col, end="")
        col += 1
    print()
    row += 1
