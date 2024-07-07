age = int(input("Enter your age:"))
have_lic = input("Do you have driving licence:Yes or No?:")

if age >= 18 and (have_lic == "yes" or "Yes"):
    print("You can drive")
else:
    print("You can't drive")
