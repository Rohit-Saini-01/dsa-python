num = int(input("Enter a number:"))
divisor = 2
flag = False

while divisor < num:
    if num % divisor == 0:
        flag = True
    divisor = divisor + 1

if flag:
    print("Entered number is not prime")
else:
    print("Entered number is prime")
