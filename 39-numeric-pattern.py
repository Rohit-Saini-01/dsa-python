num = int(input("Enter the number:"))

row = 1

while row <= num:
    col = 1
    while col <= num:
        if num + col - row >= 5:
            print(num + 1, end="")
        else:
            print(num + col - row, end="")
        col += 1
    print()
    row += 1
