# TUPLES  - similar to lists but immutable

my_tuple = (1,2,3,4,5)

print(my_tuple[1])
print(my_tuple[3])

print(5 in my_tuple)

# TUPLE METHODS 
# count , index
new_tup = (1,2,2,3,4,3,4,4,3,4)

print(new_tup.count(1))
print(new_tup.count(2))
print(new_tup.count(3))
print(new_tup.count(4))
print()

print(new_tup.index(1))
print(new_tup.index(3))
print(new_tup.index(3,4))
print(new_tup.index(3,6))
print(new_tup.index(4))
print(new_tup.index(4,7))
print()

print(len(new_tup))