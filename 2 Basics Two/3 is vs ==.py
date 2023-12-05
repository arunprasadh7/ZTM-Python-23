# difference between is vs ==

# == checks the value
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

print()

# is -checks if the memory address is same
print(True is 1)
print('' is 1)
print([] is 1)
print(10.0 is 10.0)
print([] is [])

print()

print(True is True) #both are stored in same memory location
print('1' is '1') #same memory location
print([] is []) #different memory location - all datastructures are stored in different memory location
print(10 is 10) #same ML
a = [1,2,3]
b = [1,2,3]
print(a is b) #different ML