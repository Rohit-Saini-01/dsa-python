num = int(input("Enter the value of num:"))

row = 1

while row <= num:
    col = 1

    while col <= num - row + 1:
        print(col, end="")
        col += 1

    col = 0.5
    while col <= row - 1:
        print("*", end="")
        col += 0.5

    col = num - row + 1
    while col > 0:
        print(col, end="")
        col -= 1
    print()
    row += 1
