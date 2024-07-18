num = int(input("Enter the value of num:"))

row = 1
start_char = "A"
while row <= num:
    col = 1
    while col <= num:
        print(chr(ord(start_char) + col - 1), end="")
        col += 1
    print()
    row += 1
