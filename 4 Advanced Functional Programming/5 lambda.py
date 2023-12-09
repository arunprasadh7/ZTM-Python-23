# Lambda expressions - anonymous functions, usually used if the function is used only once

my_list = [x for x in range(1, 5)]


print(list(map(lambda x: x*2, my_list)))

print(list(map(lambda x: x**2, my_list)))


# bro lambda

# double = lambda x:x+2
def double(x): return x + 2


print(double(5))

# multiply
# multiply = lambda x,y : x*y


def multiply(x, y): return x*y


print(multiply(5, 2))


# add
def add(x, y, z): return x+y+z


# add = lambda x,y,z : x+y+z
print(add(5, 5, 5))


# fullname
def fullname(fname, lname): return f'{fname} {lname}'


# fullname = lambda fname,lname : f'{fname} {lname}'
print(fullname('Arun', 'Prasadh'))

# check vote age


def age(age): return 'yes' if age > 18 else 'No'


# age = lambda age : 'Yes' if age > 18 else 'No'
print(age(10))
