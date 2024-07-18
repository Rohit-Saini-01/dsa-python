start_fah = int(input("Enter the starting value of temp in fahrenheit:"))
step = int(input("Enter the step size:"))
end_fah = int(input("Enter the ending value of temp in fahrenheit:"))


while start_fah <= end_fah:
    celsius = 5 / 9 * (start_fah - 32)
    print(start_fah, "\t", celsius)
    start_fah += step
