num = int(input("Enter the number of rows you wanna print:"))

row = 1

while row <= num:
    col = 1
    while col <= num:
        print(chr(ord("A") + col - 1), end="")
        col += 1
    print()
    row += 1
