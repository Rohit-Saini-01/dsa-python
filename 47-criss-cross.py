num = int(input("Enter the value of num:"))

row = 1
while row <= num:
    col = 1
    while col <= num:
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
        col += 1
    col = num - 1
    while col >= 1:
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
        col -= 1
    row += 1
    print()

row = num - 1
while row > 0:
    col = 1
    while col <= num:
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
        col += 1
    col = num - 1
    while col >= 1:
        if col == row:
            print(col, end="")
        else:
            print(" ", end="")
        col -= 1
    row -= 1
    print()
