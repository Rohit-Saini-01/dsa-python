num = int(input("Enter the value of num:"))
start_char = chr(ord("A") + num - 1)

row = 1
while row <= num:
    col = 1
    while col <= row:
        print(chr(ord(start_char) - row + col), end="")
        col += 1
    print()
    row += 1
