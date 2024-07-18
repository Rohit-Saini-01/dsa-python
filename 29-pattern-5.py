num = int(input("Enter the value of n:"))

row = 1
while row <= num:
    temp = 1
    col = row
    while temp <= row:
        print(col, end="")
        col += 1
        temp += 1
    print()
    row += 1
