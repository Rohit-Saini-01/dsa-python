num = int(input("Enter the value of num:"))

row = 1
while row <= num:
    col = 1
    while col <= row:
        if row == 1:
            print(1, end="")
        elif col == 1 or col == row:
            print(row - 1, end="")
        else:
            print(0, end="")
        col += 1
    print()
    row += 1
