num = int(input("Enter a number:"))
count = 2

while count <= num:
    count_2 = 2
    flag = False

    while count_2 < count:
        if count % count_2 == 0:
            flag = True
        count_2 = count_2 + 1
    if not (flag):
        print(count)
    count = count + 1
