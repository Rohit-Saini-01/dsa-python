num = int(input("Enter the value of num:"))
row = 1
while row <= num:
    col = 1
    while col <= num - row + 1:
        print(row, end="")
        col += 1
    print()
    row += 1
