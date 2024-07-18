num = int(input("Enter the number of rows you wanna print:"))

row = 1
while row <= num:
    start_char = chr(ord("A") + row - 1)
    col = 1
    while col <= num:
        print(chr(ord(start_char) + col - 1), end="")
        col += 1
    print()
    row += 1
