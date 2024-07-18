num = int(input("Enter a number:"))
num_cpy = num
rev_num = 0

while num > 0:
    rev_num = rev_num * 10 + num % 10
    num //= 10

if num_cpy == rev_num:
    print("Palindrome Number")
else:
    print("Not palindrome number")
