num = int(input("Enter the value of num:"))

row = 1
while row <= num:
    col = 1
    while col <= num - row:
        print(" ", end="")
        col += 1

    temp = row
    col = 1
    while col <= row:
        print(temp, end="")
        col += 1
        temp += 1

    temp = temp - 2
    while temp >= row:
        print(temp, end="")
        temp -= 1
    print()
    row += 1
