num_1 = 10
print(id(num_1))
num_1 = num_1 + 1
print(id(num_1))


num_1 = 10
print(id(num_1))
num_2 = 10
print(id(num_2))
# Same address for two different variables because there value is same(optimisation)

num_1 = 1000038943485757575757575757593939300000000000000000000000000000000000000000000000000000000000000
print(id(num_1))
num_2 = 1000038943485757575757575757593939300000000000000000000000000000000000000000000000000000000000000
print(id(num_2))

# Type of number values in python <class 'int'> <class 'float'> <class 'complex'>

num_1 = 10
num_2 = 10.10
num_3 = 10 + 10j

print(type(num_1))
print(type(num_2))
print(type(num_3))
