num = int(input("Enter the value of num:"))

row = num

start_char = "A"

while row > 0:
    col = 1
    while col <= row:
        print(chr(ord(start_char) + col - 1), end="")
        col += 1
    print()
    row -= 1
