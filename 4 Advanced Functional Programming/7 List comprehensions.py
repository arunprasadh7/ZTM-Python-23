# List comprehensions

my_list = []

for i in 'hello':
    my_list.append(i)

print(my_list)

# using comprehension

# my_list = [param for param in iterable]
my_list = [char for char in 'hello']
print(my_list)

my_square = [x**2 for x in range(1, 5)]
print(my_square)

mylist = [x for x in range(0, 100)]
print(mylist)
print()

mylist2 = [x*2 for x in range(0, 100)]
print(mylist2)

mylist3 = [x**2 for x in range(0, 100)]
print(mylist3)
print()

mylist4 = [x**2 for x in range(0, 100) if x % 2 == 0]
print(mylist4)
print(mylist4)
