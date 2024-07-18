num = int(input("Enter the number you want to reverse:"))

rev_num = 0

while num % 10 == 0:
    num = num // 10

while num > 0:
    rev_num = rev_num * 10 + num % 10
    num = num // 10

print(rev_num)
