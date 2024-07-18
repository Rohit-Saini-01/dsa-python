num = int(input("Enter the value of num:"))
row = 1
while row <= num:
    temp = row
    col = 1
    while col <= row:
        print(temp, end="")
        col += 1
        temp -= 1
    print()
    row += 1
