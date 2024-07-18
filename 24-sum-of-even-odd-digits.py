num = int(input("Enter a number:"))
even_count = 0
odd_count = 0

while num > 0:
    if num % 2 == 0:
        even_count += num % 10
    else:
        odd_count += num % 10
    num //= 10
print(even_count, "\t", odd_count)
