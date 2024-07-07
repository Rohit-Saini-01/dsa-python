num = 10
# num stores address not the actual number

num = 20
# num now points to a new memory address containing 20
print(num)
print(type(num))

num = "number"
# as the address to which the variable is pointing changes, python allows us to assign different types of data to the same variable
print(num)
print(type(num))
