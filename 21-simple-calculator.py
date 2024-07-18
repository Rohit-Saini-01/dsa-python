num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

choice = int(input("Enter you choice(1-6):"))

while choice != 6:
    if choice == 1:
        print(num_1 + num_2)
    elif choice == 2:
        print(num_1 - num_2)
    elif choice == 3:
        print(num_1 * num_2)
    elif choice == 4:
        print(num_1 / num_2)
    elif choice == 5:
        print(num_1 % num_2)
    else:
        print("Invalid choice!")
    choice = int(input("Enter you choice(1-6):"))
