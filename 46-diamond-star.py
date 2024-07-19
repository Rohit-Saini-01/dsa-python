num = int(input("Enter the value of num:"))

row = 1
while row <= num:
    col = 1
    while col <= num - row:
        print(" ", end="")
        col += 1
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    col = col - 2
    while col > 0:
        print("*", end="")
        col -= 1
    row += 1
    print()

row = num - 1
while row > 0:
    col = num - row
    while col >= 1:
        print(" ", end="")
        col -= 1
    col = row
    while col >= 1:
        print("*", end="")
        col -= 1

    col = row - 1
    while col > 0:
        print("*", end="")
        col -= 1
    row -= 1
    print()
